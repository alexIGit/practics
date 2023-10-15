class Component():
  def operation(self):
    pass


class ConcreteComponent(Component):
  def operation(self):
    return "Concrete Component"


class Decorator(Component):
  _component = None

  def __init__(self, component):
    self._component = component

  @property
  def component(self):
    return self._component

  def operation(self):
    return self._component.operation()


class ConcreteDecoratorA(Decorator):
  def operation(self):
    return f"ConcreteDecoratorA: {self.component.operation()}"


class ConcreteDecoratorB(Decorator):
  def operation(self):
    return f"ConcreteDecoratorB -> {self.component.operation()}"


def client_code(component):
  print(f"RESULT: {component.operation()}", end="\n\n")


if __name__ == "__main__":
  # 1
  simple = ConcreteComponent()
  print("Client: I've got a simple component:")
  client_code(simple)


  # 2
  decorator1 = ConcreteDecoratorA(simple)
  print("Client: Now I've got a decorated component:")
  client_code(decorator1)

  # 3
  decorator2 = ConcreteDecoratorB(decorator1)
  print("Client: Now I've got a decorated component:")
  client_code(decorator2)
