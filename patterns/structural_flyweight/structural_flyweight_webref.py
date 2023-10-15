class Auto:
  def __init__(self, model):
    self.model = model


class AutoFactory:
  def __init__(self):
    self.models = {}
    self.count = 0

  def create(self, name):
    model = self.models.get(name)

    if model:
      return model

    self.count = self.count + 1

    self.models[name] = Auto(name)
    return self.models[name]

  def get_models(self):
    print("Count autos: %s" % self.count)
    for model in self.models:
      print(model)

if __name__ == "__main__":
  factory = AutoFactory()

  bmw = factory.create('bmw')
  audi = factory.create('audi')
  tesla = factory.create('tesla')
  teslaBlack = factory.create('tesla')

  factory.get_models()
    