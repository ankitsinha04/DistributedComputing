from concurrent import futures
import time

import grpc

import cloud_pb2 as cloudPB
import cloud_pb2_grpc as cloudGRPC

from node import Node
import datastore
from geopy.geocoders import Nominatim
import geomap

import math

import os

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class CloudServer(cloudGRPC.CloudAPIServicer):
	def __init__(self, id, node_name, ip, port, coordinate):
		self.node = Node(id, node_name, ip, port, coordinate)
		self.geomap = geomap.Geomap()
		self.region_list = self.geomap.regional_list
		self.datastore = datastore.Datastore(id)
		self.geolocator = Nominatim(user_agent="App_Name")
		self.active_fog_nodes = []
		self.InitializeDatastore()

	def InitializeDatastore(self):
		image_list = os.listdir('./images')
		for i in image_list:
			if i == '.DS_Store':
				continue
			i=i.split('.')[0]
			photo_id =  int(i.split('-')[0])
			address = i.split('-')[1]
			self.tag(photo_id, address)

	def tag(self, photo_id, address):
		print ("The address you gave was " + address)
		try:
			geolocator = Nominatim(user_agent="specify_your_app_name_here")
			location = geolocator.geocode(address)
			self.x_coordinate = int(location.latitude)
			self.y_cooridnate = int(location.longitude)
			key = self.y_cooridnate*100+self.x_coordinate
			self.datastore.insert(key, photo_id)
		except:
			pass

	def Tag(self, request, context):
		
		geolocator = Nominatim(user_agent="geolocator1")
		location = geolocator.geocode(request.address)
		code=0
		if location==None:
			code=1
		else:
			print ("The address you gave was " + str(location.latitude) + ", " + str(location.longitude))
			self.x_coordinate = int(location.latitude)
			self.y_cooridnate = int(location.longitude)
			key = self.y_cooridnate * 100 + self.x_coordinate
			self.datastore.insert(key, request.imageId)
		
		return cloudPB.Error(code=code)
		
	def Fetch(self, request, context):
		key = int(request.coordinates.long)*100+int(request.coordinates.lat)
		data = self.datastore.get(key)
		if len(data) > 5:
			data = data[0:5]
		response = cloudPB.ResponseFetch()
		response.imageIdList.extend(data)

		return response
		

	# def RegisterFogNode(self,IP_Address):
	# 	self.active_fog_nodes.append(IP_Address)
	# 	for i in self.region_list.keys():
	# 		if IP_Address in self.region_list[i]:
	# 			return self.region_list[i]

	def RegisterFogNode(self, request, context):
		ip = request.ip
		coords = request.coordinates
		print('Register fog node at ' + ip)
		response = cloudPB.ResponseRegisterFog()
		response.regionId = 0

		self.active_fog_nodes.append(ip)
		for i in self.region_list.keys():
			if ip in self.region_list[i]:
				response.regionId = i
				response.ipList.extend(self.region_list[i])
				# print('hi')
				# return self.region_list[i]
				return response
		
		return response



def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	cloudGRPC.add_CloudAPIServicer_to_server(CloudServer(id, "Cloud", '127.0.0.1', 502, [0,0]), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

serve()