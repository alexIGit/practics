
class Memento():
 	def __init__(self, value):
 		self.value = value

def save(val):
	return Memento(val)

def restore(memento):
	print(memento.value)
	return None


class Caretaker:
	values = [];

	def add_memento(self, memento):
		self.values.append(memento)

	def get_memento(self, index):
		return self.values[index]

if __name__ == "__main__":
	caretaker = Caretaker()
	caretaker.add_memento(save('Hello!'))
	caretaker.add_memento(save('Hello world'))
	caretaker.add_memento(save('Hello awesome world'))

	restore(caretaker.get_memento(0))
	restore(caretaker.get_memento(2))


