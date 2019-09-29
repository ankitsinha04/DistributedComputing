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

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def run():
	# NOTE(gRPC Python Team): .close() is possible on a channel and should be
	# used in circumstances in which the with statement does not fit the needs
	# of the code.

	coord = cloudPB.Coordinates(lat=0, long=0)
	ip = '127.0.0.1'
	req = cloudPB.RequestRegisterFog(coordinates=coord, ip=ip)
	
	with grpc.insecure_channel('localhost:50051') as channel:
		stub = cloudGRPC.CloudAPIStub(channel)
		response = stub.RegisterFogNode(req)
		# print(response.ipList)

run()