class Equipment:
  def __init__(self):
    self.name
    self.price

  def get_name(self):
    return self.name

  def get_price(self):
    return self.price

  def set_name(self, name):
    self.name = name

  def set_price(self, price):
    self.price = price

class Engine(Equipment):
  def __init__(self):
    super()
    self.set_name('Engine')
    self.set_price(1000)

class Body(Equipment):
  def __init__(self):
    super()
    self.set_name('Body')
    self.set_price(5000)

class Composite(Equipment):
  def __init__(self):
    super()
    self.equipmets = []

  def add(self, equipmet):
    self.equipmets.append(equipmet)

  def get_price(self):
    total_price = 0

    for equipmet in self.equipmets:
      total_price = total_price + equipmet.get_price()

    # print("total price is %s" % total_price)
    return total_price

class Car(Composite):
  def __init__(self):
    super()
    self.equipmets = []
    self.set_name('audi')
    self.set_price(100500)

  def get_info(self):
    print(f"{self.name}'s price is {self.get_price()}")
    

      

if __name__ == "__main__":
  composite = Composite()   
  composite.add(Engine())
  # composite.add(Engine())

  # composite.get_price() 
  
  car = Car()
  car.add(Engine())
  car.add(Body())
  # car.get_price()
  car.get_info()

