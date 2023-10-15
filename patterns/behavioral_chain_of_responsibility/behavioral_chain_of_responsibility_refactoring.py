 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):

	@abstractmethod
	def set_next(self, handler):
		pass

	@abstractmethod
	def handle(self, request):
		pass


class AbstractHandler(Handler):
	_next_handler = None

	def set_next(self, handler):
		self._next_handler = handler
		return handler

	@abstractmethod
	def handle(self, request):
		if self._next_handler:
			return self._next_handler.handle(request)
		return None


class MonckeyHandler(AbstractHandler):
	def handle(self, request):
		if request == "Banana":
			return f"Monkey: I'll eat the {request}"
		else:
			return super().handle(request)


class SquirreHandler(AbstractHandler):
	def handle(self, request):
		if request == "Nut":
			return f"Squirre: I'll eat the {request}"
		else:
			return super().handle(request)


class DogHandler(AbstractHandler):
	def handle(self, request):
		if request == "MeatBall":
			return f"Dog: I'll eat the {request}"
		else:
			return super().handle(request)

def client_code(handler):
	for food in ["Nut", "Banana", "Cup of coffee"]:
		print(f"\nClient: Who wants a {food}?")
		result = handler.handle(food)

		if result:
			print(f"    {result}", end="")
		else:	
			print(f"    {food} was left untouched", end="")

	print('\n')


if __name__ == "__main__":
	monkey = MonckeyHandler()
	squirre = SquirreHandler()
	dog = DogHandler()

	monkey.set_next(squirre).set_next(dog)


	print("Chain: Monkey > Squirrel > Dog")
	client_code(monkey)


	print("Subchain: Squirrel > Dog")
	client_code(squirre)

