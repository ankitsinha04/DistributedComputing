from concurrent import futures
import time

import grpc

import cloud_pb2 as cloudPB
import cloud_pb2_grpc as cloudGRPC

import fog_pb2 as fogPB
import fog_pb2_grpc as fogGRPC

import fog as fog

cloudIP = 'localhost:50051'

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

with grpc.insecure_channel('localhost:50050') as channel:
	stub = fogGRPC.FogAPIStub(channel)
	coords = fogPB.Coordinates(lat=48, long=2)
	req = fogPB.RequestFetch(imageId=1022, coordinates=coords)
	response = stub.Fetch(req)
	print(response.imageIdList)
	channel.close()
