from abc import ABC, abstractmethod

class AbstractClass(ABC):
	def template_method(self):
		self.base_operation1()
		self.required_operation1()
		self.base_operation_2()
		self.hook1()
		self.required_operation2()
		self.base_operation3()
		self.hook2()

	def base_operation1(self):
		print("AbstractClass says: 1 -> I am doing the bulk of the work")


	def base_operation_2(self):
		print("AbstractClass says: 2 -> But I let subclasses override some operations")

	def base_operation3(self):
		print("AbstractClass says: 3 -> I am doing the bulk of the work")

	@abstractmethod
	def required_operation1(self):
		pass

	@abstractmethod
	def required_operation2(self):
		pass

	def hook1(self):
		pass

	def hook2(self):
		pass




class ConcreteClass1(AbstractClass):
	def required_operation1(self):
		print("ConcreteClass1 says: Implemented Operation1")

	def required_operation2(self):
		print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
	def required_operation1(self):
		print("ConcreteClass2 says: Implemented Operation1")

	def required_operation2(self):
		print("ConcreteClass2 says: Implemented Operation2")

	def hook1(self):
		print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class):
	abstract_class.template_method()
	print('\n')

if __name__ == "__main__":
	print("Same client code can work with different subclasses:")
	client_code(ConcreteClass1())

	print("Same client code can work with different subclasses:")
	client_code(ConcreteClass2())

