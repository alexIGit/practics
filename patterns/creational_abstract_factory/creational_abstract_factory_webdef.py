#  Elements
class sportCars():
  def __init__(self, name):
    self.name = name

  def get_info(self):
    info = f'{self.name} \tis a sport car!'
    print(info)
    return info

class familyCars():
  def __init__(self, name):
        self.name = name

  def get_info(self):
    info = f'{self.name} \t\tis a family car!'
    print(info)
    return info


# Factories

def sportCarFactory():
  return sportCars('Lamborgini')

def familyCarFactory():
  return familyCars('Skoda')

# Abstract factory

def carProducer(kind):
  if kind == 'sport':
    return sportCarFactory
  else:
    return familyCarFactory
  


def webdef_name():
  car = sportCars('Lamborgini')
  car.get_info()

  car_1 = familyCars('Skoda')
  car_1.get_info()

  # with Abstract factory
  print('\n')

  produce_sport = carProducer('sport')
  car_sport = produce_sport()
  car_sport.get_info()
  

  produce_car = carProducer('no sport')
  car = produce_car()
  car.get_info()
  print('\n')


# gamma_name
#  Elements
class ConcreteProduct_1():
  def __init__(self, name):
    self.name = name

  def get_info(self):
    info = f'It is a \t{self.name}'
    print(info)
    return info

class ConcreteProduct_2():
  def __init__(self, name):
        self.name = name

  def get_info(self):
    info = f'It is a \t{self.name}'
    print(info)
    return info


# Factories

def ConcreteFactory_1():
  return ConcreteProduct_1('name -> ConcreteProduct_1')

def ConcreteFactory_2():
  return ConcreteProduct_2('name -- ConcreteProduct_2')

# Abstract factory

def AbstractFactory(kind):
  if kind == 'product_1':
    return ConcreteFactory_1
  else:
    return ConcreteFactory_2

def gamma_name():
  producer = AbstractFactory('product_1')
  product_1 = producer()
  product_1.get_info()

  producer_2 = AbstractFactory('product_2')
  product_2 = producer_2()
  product_2.get_info()



if __name__ == '__main__':
  webdef_name()
  gamma_name()
