import json
from typing import Dict

class Flyweight():
	def __init__(self, shared_state):
		self._shared_state = shared_state

	def operation(self, unique_state):
		s = json.dumps(self._shared_state)
		u = json.dumps(unique_state)
		print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="\n")


class FlyweightFactory():
	_flyweights = {}

	def __init__(self, initial_flygweghts):
		for state in initial_flygweghts:
			self._flyweights[self.get_key(state)] = Flyweight(state)

	def get_key(self, state):
		return "_".join(sorted(state))

	def get_flyweight(self, shared_state):
		key = self.get_key(shared_state)

		if not self._flyweights.get(key):
			print("FlyweightFactory: Can't find a flyweight, creating new one.\n")
			self._flyweights[key] = Flyweight(shared_state)
		else:
			print("FlyweightFactory: Reusing existing flyweight.\n")

		return self._flyweights[key]


	def list_flyweghts(self):
		count = len(self._flyweights)
		print(f"FlyweightFactory: I have {count} flyweights:")
		print("\n".join(map(str, self._flyweights.keys())), end="\n")




def add_car_to_police_database(factory, plates, owner, brand, model, color):
	print("\n\nClient: Adding a car to database.")
	
	flyweight = factory.get_flyweight([brand, model, color])		

	flyweight.operation([plates, owner])

if __name__ == "__main__":

	factory = FlyweightFactory([
		["Chevrolet", "Camaro2018", "pink"],
		["Mercedes Benz", "C300", "black"],
		["Mercedes Benz", "C500", "red"],
		["BMW", "M5", "red"],
		["BMW", "X6", "white"],
    ])

	factory.list_flyweghts()

	add_car_to_police_database(factory, "cl244", "James", "BMW", "M5", "red")
	add_car_to_police_database(factory, "cl244", "James", "BMW", "M5", "red")
	add_car_to_police_database(factory, "clk", "joy", "Mers", "cel", "blue")



	factory.list_flyweghts()