
from node import Node
import datastore
from geopy.geocoders import Nominatim
import geomap
import math
import os

class Cloud:
	
	def __init__(self, id, node_name, ip, port, coordinate):
		self.node = Node(id, node_name, ip, port, coordinate)
		self.geomap = geomap.Geomap()
		self.region_list = self.geomap.regional_list
		self.geolocator = Nominatim(user_agent="App_Name")
		self.active_fog_nodes = []
		self.datastore= datastore.Datastore(id)
		print self.datastore.get_id()
		self.InitializeDatastore()
	
	def InitializeDatastore(self):
		image_list = os.listdir('./Images')
		for i in image_list:
			if i == '.DS_Store':
				continue
			i=i.split('.')[0]
			photo_id =  int(i.split('-')[0])
			address = i.split('-')[1]
			self.tag(photo_id, address)
		

	def tag(self, photo_id, address):
		print "The address you gave was " + address
		geolocator = Nominatim(user_agent="specify_your_app_name_here")
		location = geolocator.geocode(address)
		self.x_coordinate = int(location.latitude)
		self.y_cooridnate = int(location.longitude)
		key = self.y_cooridnate*100+self.x_coordinate
		self.datastore.insert(key, photo_id)

	def fetch(self, photo, latitude, longitude):
		key = int(longitude)*100+int(latitude)
		data = self.datastore.get(key)
		if len(data)>5:
			data=data[0:5]
		return data 
	

	def RegisterFogNode(self,IP_Address):
		self.active_fog_nodes.append(IP_Address)
		for i in self.region_list.keys():
			if IP_Address in self.region_list[i]:
				return self.region_list[i]
		
		

Cloud=Cloud(0, "Cloud", '0.0.0.0', 502, [0,0])
