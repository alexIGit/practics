# базовый класс
class Car:
  def __init__(self):
    self.autoPilot = False
    self.parktronic = False

  def __str__():
    return 'It is a Car'

# builder
class CarBuilder:
  def __init__(self, name='un_name'):
    self.name = name
    self.car = Car()

  def addAutopilot(self, isItAutoPilot):
    self.car.autoPilot = isItAutoPilot
    return self

  def addParktronic(self, isItParktronic):
    self.car.parktronic = isItParktronic
    return self

  def updateEngine(self, engine):
    self.car.engine = engine
    print(f'{self.name} engine update to version {engine}')
    return self

  def build(self):
    car_info = f"""
      car name is {self.name}
      autoPilot: {self.car.autoPilot}
      parktronic: {self.car.parktronic}
    """
    if hasattr(self.car, 'engine'):
      car_info = f"""
        {car_info}
        engine: {self.car.engine}
      """

    print(car_info)
    return self.car

  def __str__(self):
    return self.name

def main():
  car_webdef = CarBuilder().build()

  car_webdef_mod_1 = CarBuilder('BMW')
  car_webdef_mod_1.addAutopilot(True)
  car_webdef_mod_1.addParktronic(True)
  car_webdef_mod_1.build()

  car_webdef_mod_2 = CarBuilder('Ferrari')
  car_webdef_mod_2.updateEngine('V8')
  car_webdef_mod_2.build()

  print(car_webdef_mod_2)

  mod_s = CarBuilder('mod_s')
  print(mod_s)
  


if __name__ == '__main__':
  main()
