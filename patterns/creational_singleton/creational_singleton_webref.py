
class Counter:
  def __init__(self, name):
    self.name = name
      
    self.count = 0

  def increase_count(self):
    self.count = self.count + 1
    # return


  def get_count(self):
    print(f"{self.name}: count: {self.count}")

if __name__ == "__main__":
  count1 = Counter('count1') 
  count2 = Counter('count2') 

  # пока мне не понятно
  # id-шки должны быть одинаковыми или разными 

  print(f"id count1: {id(count1)}")
  print(f"id count2: {id(count2)}")

  count1.increase_count()
  count1.increase_count()
  count2.increase_count()
  count1.increase_count()

  count1.get_count()
  count2.get_count()
