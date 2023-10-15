class TeslaCar:
  def __init__(self, model, price):
    self.model = model
    self.price = price

  def produce(self):
    return TeslaCar(self.model, self.price)

  def get_info(self):
    print(f"""
      model: {self.model}
      price: {self.price}
    """, end="\n")

if __name__ == '__main__':
  prototypeCar = TeslaCar('S', 1000)

  car1 = prototypeCar.produce()
  car2 = prototypeCar.produce()

  car1.get_info()
  car1.price = '20000'
  car1.get_info()


  car2.get_info()
  car2.model = 'E2'
  car2.get_info()
