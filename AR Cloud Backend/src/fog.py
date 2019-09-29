from concurrent import futures
import time

import grpc

import cloud_pb2 as cloudPB
import cloud_pb2_grpc as cloudGRPC

import fog_pb2 as fogPB
import fog_pb2_grpc as fogGRPC

import cache as cache

cloudIP = 'localhost:50051'

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class FogServer:
	
	def __init__(self, Fog_Name , longitude, latitude , IP_Address):
		self.Name = Fog_Name
		self.coordinates = cloudPB.Coordinates(lat=int(longitude)+180, long=int(latitude)+90)
		self.ip = IP_Address
		self.cache = cache.Cache()

		self.attachToCloud(cloudIP)
	
	def attachToCloud(self, cloudIP):
		coord = self.coordinates
		ip = self.ip
		req = cloudPB.RequestRegisterFog(coordinates=coord, ip=ip)
		
		with grpc.insecure_channel(cloudIP) as channel:
			stub = cloudGRPC.CloudAPIStub(channel)
			response = stub.RegisterFogNode(req)
			self.regionId = response.regionId
			self.regionalFogList = response.ipList
			channel.close()
	
	def tagInCloud(self, imageId, address):
		req = cloudPB.RequestTag(imageId = imageId, address = address)
		with grpc.insecure_channel(cloudIP) as channel:
			stub = cloudGRPC.CloudAPIStub(channel)
			response = stub.Tag(req)
			channel.close()

	def fetchFromCloud(self, imageId, latitude, longitude):
		coords = cloudPB.Coordinates(lat=latitude, long=longitude)
		req = cloudPB.RequestFetch(imageId = imageId, coordinates=coords)
		with grpc.insecure_channel(cloudIP) as channel:
			stub = cloudGRPC.CloudAPIStub(channel)
			response = stub.Fetch(req)
			print(response.imageIdList)
			channel.close()

	def Fetch(self, request, context):
		imageId = request.imageId
		latitude = request.coordinates.lat
		longitude = request.coordinates.long
		ret = []

		imageIdList = self.cache.search(imageId, latitude, longitude)
		if imageIdList == None:
			response = self.fetchFromCloud(image, latitude, longitude)
			ret = response.imageIdList
			if not ret == []:
				self.cache.set(latitude, longitude, ret)
		else:
			ret = imageIdList

		userResponse = fogPB.ResponseFetch(imageIdList=ret)
		return userResponse


# fog = Fog('Fog_Computer_1', -90, +90, 'localhost:50050')

# fog.tagInCloud(1022, 'Eiffel Tower, Paris, France')

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	fogGRPC.add_FogAPIServicer_to_server(FogServer('Fog_Computer_1', -90, +90, 'localhost:50050'), server)
	server.add_insecure_port('[::]:50050')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

serve()
# fog.Fetch(1022, 48, 2)