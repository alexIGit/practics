class Car:
  def __init__(self):
    self.price = 100
    self.model = 'car'

  def get_price(self):
    return self.price

  def get_description(self):
    return self.model


class Tesla(Car):
  def __init__(self):
    super()
    self.price = 500
    self.model = 'tesla'

# decorators
class Autopilot:
  def __init__(self, car):
    self.car = car

  def get_price(self):
    return self.car.get_price() + 1001

  def get_description(self):
    return (f"{self.car.get_description()} with autopilot")


if __name__ == "__main__":
  tesla = Tesla()

  tesla = Autopilot(tesla)
  print(f"{tesla.get_description()}. Price: {tesla.get_price()}")
