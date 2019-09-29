import math

class Geomap:
	
	def __init__(self):
		self.fog_locations = [[[] for x in range(0,181)] for y in range(0,361)]
		self.regional_list={}
		self.InitializeFogLocations('Fog_Locations.json')


	def InitializeFogLocations(self, file_name):
		f = open(file_name ,'rb')
		for x in f:
			x=x.decode()
			if x== '\n':
				continue
			Fog_name = x.split(' ')[:-1][0]
			latitude = int(math.ceil(float(x.split(' ')[:-1][1])))
			longitude =int(math.ceil(float(x.split(' ')[:-1][2])))
			IP_Address = x.split(' ')[:-1][3]
			fog_desc= Fog_Descriptor(Fog_name, IP_Address, latitude, longitude)
			if fog_desc.region in self.regional_list.keys():
				self.regional_list[fog_desc.region].append(IP_Address)
			else:
				self.regional_list[fog_desc.region] = [IP_Address]
			self.fog_locations[longitude+180][latitude+90].append(fog_desc)	
			
			
	def addFogNode(self,fog_name,latitude,longitude,Ip_Address):
		fog_desc= Fog_Descriptor(fog_name, Ip_Address, latitude, longitude)
		self.fog_locations[int(longitude)+180][int(latitude)+90].append(fog_desc)	
		return regions[fog_desc.region]
		

class Fog_Descriptor:
	
	def __init__(self, Fog_Name, IP_Address, latitude,longitude):
		self.Name = Fog_Name
		self.coordinates =[int(longitude)+180 , int(latitude)+90]
		self.IP_Addr = IP_Address
		self.region = self.assignRegion()
		
	
	def assignRegion(self):
		latitude = self.coordinates[1]-90
		longitude = self.coordinates[0]-180
		if latitude>=0 and longitude>=0
			return 0
		elif latitude>=0 and longitude<0:
			return 1
		elif latitude<0 and longitude<0:
			return 2
		else:
			return 3
			

x=Geomap()
	
	
	