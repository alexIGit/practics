class Model:
  def __init__(self, color):
    self.color = color

class Color:
  def __init__(self, type):
    self.type = type

  def get(self):
    # print(self.type)
    return self.type


class BlackColor(Color):
  def __init__(self):
    super().__init__("dark-black")

class SilbrigColor(Color):
  def __init__(self):
    super().__init__("silbermetallic")

class Audi(Model):
  def __init__(self, color):
    super().__init__(color)

  def paint(self):
    print(f"Auto: Audi, Color: {self.color.get()}")

class Bmw(Model):
  def __init__(self, color):
    super().__init__(color)

  def paint(self):
    print(f"Auto: Bmw, Color: {self.color.get()}")


if __name__ == "__main__":
  blackBmw = Bmw(BlackColor())
  blackBmw.paint()
