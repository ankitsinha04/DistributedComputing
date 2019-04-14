
class Node:
	
	def __init__(self,id,node_name,ip,port,coordinate):
		self.id = id
		self.name = node_name
		self.ip=ip
		self.port = port
		self.coordinate=coordinate
		

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name


		