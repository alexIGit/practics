from abc import ABC, abstractmethod
# Elements
class Product(ABC):
  
  @abstractmethod
  def operation(self):
    pass


class ConcreteProduct1(Product):
  def operation():
    return "{Result of the ConcreteProduct1}"   

class ConcreteProduct2(Product):
  def operation():
    return "{Result of the ConcreteProduct2}"   
# 

class Creator(ABC):
    
  @abstractmethod
  def factory_method(self):
    pass

  def some_operation(self):
    product = self.factory_method()
    result = f"Creator: The same creator's code has just worked with {product.operation()}"

    return result

class ConcreteCreator1(Creator):
  def factory_method(self):
    return ConcreteProduct1

class ConcreteCreator2(Creator):
  def factory_method(self):
    return ConcreteProduct2
        

def client_code(creator):
      
  print(f"{creator.some_operation()}", end="\n")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
