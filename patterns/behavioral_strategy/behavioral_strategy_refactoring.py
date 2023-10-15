from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context:
 	def __init__(self, strategy):
 		self._strategy = strategy

 	@property
 	def strategy(self):
 		return self._strategy

 	@strategy.setter
 	def strategy(self, strategy):
 		self._strategy = strategy


 	def do_something_business_logic(self):
 		print("Context: Sorting data using the strategy (not sure how it'll do it)")
 		result = self._strategy.do_algoritm(['a', 'b', 'c', 'd', 'e'])
 		print(",".join(result))


class Strategy(ABC):
	@abstractmethod
	def do_algoritm(self, data):
		pass

class ConcreteStrategyA(Strategy):
	def do_algoritm(self, data):
		return sorted(data)


class ConcreteStrategyB(Strategy):
	def do_algoritm(self, data):
		return reversed(data)


if __name__ == "__main__":
	context = Context(ConcreteStrategyA())
	print("Client: Strategy is set to normal sorting.")
	context.do_something_business_logic()

	print('\nClient: Strategy is set to reverse sorting.')
	context.strategy = ConcreteStrategyB()
	context.do_something_business_logic()