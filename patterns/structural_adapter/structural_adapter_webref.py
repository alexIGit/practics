
class Engine:
  def __init__(self, name='Engine 2.0'):
    self.name = name
  
  def simpleInterface(self):
    print(f"{self.name} - tr-tr-tr")


class EngineV8:
  def __init__(self, name='Engine V8'):
    self.name = name

  def complecatedInterface(self):
    print(f"{self.name} - wriim wroom!")


class Auto:
  def __init__(self, name='simple engine'):
    self.name = name

  def startEngine(self, engine=Engine):
      engine.simpleInterface()


class EngineV8Adapter:
  def __init__(self, name, engine):
    self.name = name
    self.engine = engine

  def simpleInterface(self):
    self.engine.complecatedInterface(self)
      

if __name__ == "__main__":
  # engine 2.0
  car  = Auto()
  simpleEngine = Engine()
  car.startEngine(simpleEngine)

  # engine v8 with adapter
  adaptCar = Auto('new car')
  engineAdapter = EngineV8Adapter('adapt engine v8', EngineV8)
  adaptCar.startEngine(engineAdapter)

  # engine v8 without adapter
  noAdaptCar = Auto()
  engineV8 = EngineV8()
  # noAdaptCar.startEngine(engineV8) # -> error

