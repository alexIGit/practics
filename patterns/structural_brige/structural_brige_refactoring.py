from __future__ import annotations
from abc import ABC, abstractmethod

class Abstarction:
  def __init__(self, implementation):
    self.implementation = implementation

  def operation(self):
    return (f"Abstraction: base operation {self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstarction):
  def operation(self):
    return (f"ExtendedAbstraction: Extended base operation {self.implementation.operation_implementation()}")


class Implementation(ABC):

  @abstractmethod
  def operation_implementation(self):
    pass


class ConcreteImplementationA(Implementation):
  def operation_implementation(self):
    return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
  def operation_implementation(self):
    return "ConcreteImplementationBD: Here's the result on the platform BS."


def client_code(abstraction):
  print(abstraction.operation(), end="\n\n")


if __name__ == "__main__":
  implementation = ConcreteImplementationA()
  abstraction = Abstarction(implementation)
  client_code(abstraction)

  implementation = ConcreteImplementationB()
  abstraction = ExtendedAbstraction(implementation)
  client_code(abstraction)

