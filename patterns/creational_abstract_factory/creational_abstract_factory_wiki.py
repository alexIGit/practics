"""
https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%B0%D1%8F_%D1%84%D0%B0%D0%B1%D1%80%D0%B8%D0%BA%D0%B0_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
"""

from abc import ABCMeta, abstractmethod

class Beer(metaclass=ABCMeta):
  pass


class Snack(metaclass=ABCMeta):

  @abstractmethod
  def interact(selfself, beer: Beer) -> None:
    pass


class AbstractShop(metaclass=ABCMeta):

  @abstractmethod
  def buy_beer(self) -> Beer:
    pass

  @abstractmethod
  def buy_snack(self) -> Snack:
    pass

class Tuborg(Beer):
  pass

class Staropramen(Beer):
  pass

class Peanuts(Snack):

  def interact(self, beer: Beer) -> None:
    print(f"Мы выпили по бутылке пива {beer.__class__.__name__} и закусили его арахисом")


class Chips(Snack):

  def interact(self, beer: Beer) -> None:
    print(f"Мы выпили несколько банок пива {beer.__class__.__name__} и съели пачку чипсов")


class ExpensiveShop(AbstractShop):

  def buy_beer(self) -> Beer:
    return Tuborg()

  def buy_snack(self) -> Snack:
    return Peanuts()


class CheapShop(AbstractShop):

  def buy_beer(self) -> Beer:
    return Staropramen()

  def buy_snack(self) -> Snack:
    return Chips()


if __name__ == '__main__':
  expensive_shop = ExpensiveShop()
  cheap_shop = CheapShop()
  print('OUTPUT:')

  beer = expensive_shop.buy_beer()
  snack = cheap_shop.buy_snack()
  snack.interact(beer)

  beer = cheap_shop.buy_beer()
  snack = expensive_shop.buy_snack()
  snack.interact(beer)
