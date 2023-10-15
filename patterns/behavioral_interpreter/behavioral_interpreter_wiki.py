__doc__  = '''
	Система для вычисления и манипулирования булевыми выражениями. Пример из книги 
	Gang of Four - "Design Patterns: Elements of Reusable Object-Oriented Software"
	'''


from abc import ABCMeta, abstractmethod


class Context:
	def __init__(self, variables = {}):
		self._variables = variables


	class ContextException(Exception):
		pass

	def lookup(self, name):
		if name in self._variables:
			return self._variables[name]

		raise self.ContextException("Heизвестная переменная {}".format(name))

	def assign(self, name, value):
		self._variables[name] = value
	

class BooleanExp(metaclass=ABCMeta):
	@abstractmethod
	def evaluate(self, context):
		pass


class ConstantExp(BooleanExp):
	def __init__(self, value):
		self._value = value

	def evaluate(self, context):
		return self._value


class VariableExp(BooleanExp):
	def __init__(self, name):
		self._name = name

	def evaluate(self, context):
		return context.lookup(self._name)



class BinaryOperationExp(BooleanExp, metaclass=ABCMeta):
	def __init__(self, left, right):
		self._left = left
		self._right = right


class AndExp(BinaryOperationExp):
	def evaluate(self, context):
		return self._left.evaluate(context) and self._right.evaluate(context)


class OrExp(BinaryOperationExp):
	def evaluate(self, context):
		return self._left.evaluate(context) or self._right.evaluate(context)


class NotExp(BinaryOperationExp):
	def __init__(self, operand):
		self._operand = operand

	def evaluate(self, context):
		return not self._operand.evaluate(context) 


def execute_test(context, x, y):
	context.assign('x', x)	
	context.assign('y', y)

	expression = OrExp(
		AndExp(ConstantExp(True), VariableExp('x')),
		AndExp(VariableExp('y'), NotExp(VariableExp('x')))

	)

	print(expression.evaluate(context))	

if __name__ == "__main__":
	context = Context()

	execute_test(context, True, False)
	execute_test(context, False, True)
	execute_test(context, False, False)
