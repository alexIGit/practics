class Bmw:
  def __init__(self, model, price):
    self.model = model
    self.price = price

  def get_info(self):
    print(f"""
      model: {self.model}
      price: {self.price}
    """, end='\n')

class BmwFactory:
  def create(self, model):
    if model == 'x5':
      return Bmw(model, 100)

    if model == 'x6':
      return Bmw(model, 200)

    return Bmw('standart', 50)
    
    
            



if __name__ == '__main__':
  factory = BmwFactory()

  x5 = factory.create('x5')
  x6 = factory.create('x6')
  st = factory.create('')

  x5.get_info()
  x6.get_info()
  st.get_info()


