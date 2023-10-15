class Conveyor:
  def set_body(self):
    print('body set!')

  def get_engine(self):
    print('Dismantle Engine!')

  def set_engine(self):
    print('engine set!')

class ConveyorFasade:
  def __init__(self, car):
    self.car = car

  def assemble_car(self):
    self.car.set_body()
    self.car.set_engine()

  def change_engine(self):
    self.car.get_engine()
    self.car.set_engine()
        

if __name__ == "__main__":
  # conveyor = Conveyor()
  conveyorFasade = ConveyorFasade(Conveyor())

  car = conveyorFasade.assemble_car()
  car = conveyorFasade.change_engine()
