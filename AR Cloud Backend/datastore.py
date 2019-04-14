
class Datastore:
	
	def __init__(self , id):
		self.id = id
		self.directory = {}
		
	def get_id(self):
		return self.id
	
	def insert(self, key, tag):
		if key in self.directory.keys():
			temp = self.directory[key]
			temp.append(tag)
			self.directory[key]=temp	
		else:
			self.directory[key] =[tag]
		
	def remove(self,key):
		pass
	
	def get(self,key):
		return self.directory[key]
	
	
		