import random

class Cache:
	
	def __init__(self):
		self.eviction_strategy = 0
		self.cache_size = 10
		self.cache_store = {}
		self.LRUList=[]
		
	def search(self, photo, latitude, longitude):
		key = int(longitude)*100+int(latitude)
		if key in self.cache_store.keys():
			data = self.cache_store[key]
			if len(data)>5:
				data=data[0:5]
			if key in self.LRUList:
				del self.LRUList[self.LRUList.index(key)]
			self.LRUList.append(key)

			return data 
		else:
			return None
		
	def set(self, key, data):
		if key in self.cache_store.keys():
			return
		if len(self.cache_store.keys())<self.cache_size:
			self.cache_store[key]=data
		else:
			if self.eviction_strategy==0:
				self.randomEvict()
			else:
				self.LRUevict()
			self.cache_store[key]=data
	
	def randomEvict(self):
		key_list =  self.cache_store.keys()
		rand = random.choice(key_list)
		del self.cache_store[rand]
		return 
	
	def LRUevict(self):
		key = self.LRUList[0]
		del self.cache_store[key]
		del self.LRUList[0]
		return 
		
		
		