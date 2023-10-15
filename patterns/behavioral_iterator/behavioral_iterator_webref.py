class ArrayIterator:
	def __init__(self, el):
		self.index = 0
		self.elements = el 

	def next(self):
		element = self.elements[self.index]
		self.index += 1
		return element

	def hasNext(self):
		isHasNext = self.index < len(self.elements)
		return isHasNext


class ObjectIterator:
	def __init__(self, el):
		self.index = 0
		self.elements = el 
		self.keys = el.keys()

	def next(self):
		# print(self.elements)
		# print(self.keys)
		# print(list(self.keys)[0])
		# print(list(self.keys[0]))


		element = self.elements[list(self.keys)[self.index]]
		# element = None
		self.index += 1
		return element

	def hasNext(self):
		isHasNext = self.index < len(self.keys)
		# print('isHasNext: \t%s' % isHasNext)
		return isHasNext		




if __name__ == "__main__":
	collection = ArrayIterator(['audi', 'bmw', 'tesla'])

	while collection.hasNext():
		print(collection.next())


	autos = {
		'audi': {
			'model': 'audi',
			'color': 'black'
		},
		'bmw': {
			'model': 'bmw',
			'color': 'red'
		},
		'tesla': {
			'model': 'tesla',
			'color': 'blue'
		}
	}

	

	# for key,values in autos.items():
	# 	print(autos[key])

	# print(autos.keys())

	# print(len(autos.keys()))

	collectionObj = ObjectIterator(autos)

	while collectionObj.hasNext():
		print(collectionObj.next())



