from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
  
  @property
  def parent(self):
    return self._parent

  @parent.setter
  def parent(self, parent):
    self._parent = parent

  def add(self, component):
    pass

  def remove(self, component):
    pass

  def is_composite(self):
    return False

  @abstractmethod
  def operation(self):
    pass

class Leaf(Component):
  def operation(self):
    return "Leaf"

class Composite(Component):
  def __init__(self):
    self._children = []

  def add(self, component):
    self._children.append(component)
    component.parent = self

  def remove(self, component):
    self._children.remove(component)
    component._parent = None

  def is_composite(self):
    return True

  def operation(self):
    results = []
    
    for child in self._children:
      results.append(child.operation())
    
    return f"Branch({'+'.join(results)})"

def client_code(component):
  print(f"RESULT: {component.operation()}", end="\n\n")


def client_code2(component1, component2):
      
  if component1.is_composite():
    component1.add(component2)
  
  print(f"RESULT: {component1.operation()}", end="\n\n")
      
if __name__ == "__main__":
  # 1
  simple = Leaf()
  print("Client: I've got a simple component:")
  client_code(simple)

  # 2
  tree = Composite()

  branch1 = Composite()
  branch1.add(Leaf())
  branch1.add(Leaf())

  branch2 = Composite()
  branch2.add(Leaf())


  tree.add(branch1)
  tree.add(branch2)

  print("Client: Now I've got a composite tree:")
  client_code(tree)

  # 3
  print("Client: I don't need to check the components classes even when managing the tree:")
  client_code2(tree, simple)
