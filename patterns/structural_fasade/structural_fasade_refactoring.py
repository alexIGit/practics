from __future__ import annotations

class Subsystem1:
  def operation1(self):
    return "Subsystem1: Ready!"

  def operation_n(self):
    return "Subsystem1: Go!"


class Subsystem2:
  def operation1(self):
    return "Subsystem2: Ready!"

  def operation_z(self):
    return "Subsystem2: Fire!"

class Fasade:
  def __init__(self, subsystem1=Subsystem1(), subsystem2=Subsystem2()):
    self._subsystem1 = subsystem1
    self._subsystem2 = subsystem2

  def operation(self):
    results = []
    results.append("Facade initializes subsystems:")
    results.append(self._subsystem1.operation1())
    results.append(self._subsystem2.operation1())

    results.append("Facade orders subsystems to perform the action:")
    results.append(self._subsystem1.operation_n())
    results.append(self._subsystem2.operation_z())
    
    return "\n".join(results)


def client_code(fasade):
  print(facade.operation(), end="\n\n")


if __name__ == "__main__":
  # 1
  subsystem1 = Subsystem1()
  subsystem2 = Subsystem2()
  facade = Fasade(subsystem1, subsystem2)
  client_code(facade)

  # 2
  client_code(Fasade())
