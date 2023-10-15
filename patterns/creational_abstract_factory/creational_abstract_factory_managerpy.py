class AbstractFactory(object):
  def create_drink(self):
    raise NotImplementedError()

  def create_food(self):
    raise NotImplementedError()

class Drink(object):
    def __init__(self, name):
      self._name = name

    def __str__(self):
      return self._name
      
class Food(object):
    def __init__(self, name):
      self._name = name

    def __str__(self):
      return self._name


class ConcreteFactory1(AbstractFactory):
  def create_drink(self):
    return Drink('Coca-cola')

  def create_food(self):
    return Food('Hamburger')

class ConcreteFactory2(AbstractFactory):
  def create_drink(self):
    return Drink('Pepsi')

  def create_food(self):
    return Food('Cheeseburger')


factory_1 = ConcreteFactory1()
factory_2 = ConcreteFactory2()


print(factory_1.create_drink())
print(factory_1.create_food())
print('\n')
print(factory_2.create_drink())
print(factory_2.create_food())
