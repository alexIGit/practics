from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample 
from string import ascii_letters, digits 

class Originator():
	_state = None

	def __init__(self, state):
		self._state = state

	def do_something(self):
		print("Originator: I'm doing something important.")
		self._state = self._generate_random_string(30)
		print(f"Originator: and my state has changed to: {self._state}")


	def _generate_random_string(self, length = 10):
		return "".join(sample(ascii_letters, length))

	def save(self):
		return ConcreteMemento(self._state)

	def restore(self, memento):
		self._state = memento.get_state()
		print(f"Originator: My state has changed to: {self._state}")



class Memento(ABC):

	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def get_date(self):
		pass


class ConcreteMemento(Memento):
	def __init__(self, state):
		self._state = state
		self._date = str(datetime.now())[:19]

	def get_state(self):
		return self._state

	def get_name(self):
		return f"{self._date} / ({self._state[0:9]}...)"

	def get_date(self):
		return self._date



class Caretaker():
	def __init__(self, originator):
		self._mementos = []
		self._originator = originator

	def backup(self):
		self._mementos.append(self._originator.save())

	def show_history(self):
		print("\nCaretaker: Here's the list of mementos:")

		for memento in self._mementos:
			print(memento.get_name())

	def undo(self):
		if not len(self._mementos):
			return

		memento = self._mementos.pop()
		print(f"Caretaker: Restoring state to: {memento.get_name()}")

		try:
			self._originator.restore(memento)
		except Exception:
			self.undo()




if __name__ == "__main__":
	originator = Originator("super-super-rrrrrrrrrrrr.")
	caretaker = Caretaker(originator)

	caretaker.backup()
	originator.do_something()

	caretaker.backup()
	originator.do_something()

	caretaker.backup()
	originator.do_something()


	caretaker.show_history()

	print("\nClient: Now, let's rollback!\n")
	caretaker.undo()
	caretaker.show_history()

	print("\nClient: Once more!\n")
	caretaker.undo()
	caretaker.show_history()








