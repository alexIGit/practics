class Stack:

  def __init__(self):
    self._stack = []

  def push(self, x):
    self._stack.append(x)

  def pop(self):
    x = self._stack.pop()
    return x

  def clear(self):
    self._stack.clear()

  def is_empty(self):
    return len(self._stack) == 0




if __name__ == "__main__":
  import doctest
  stack = Stack()
  doctest.testmod()

