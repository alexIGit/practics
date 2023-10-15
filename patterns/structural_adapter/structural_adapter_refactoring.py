class Target():
  def request(self):
    return "Target: the default target's behavior"


class Adaptee:
  def specific_request(self):
    return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
  def __int__(self, adaptee):
    self.adaptee = adaptee

  def request(self):
    return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target):
  print(target.request(), end="\n\n")

if __name__ == "__main__":
  print("Client: I can work just fine with the Target objects:")
  target = Target()
  client_code(target)

  adaptee = Adaptee()
  print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
  print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")


  print("Client: But I can work with it via the Adapter:")
  adapter = Adapter(adaptee)
  client_code(adapter)
