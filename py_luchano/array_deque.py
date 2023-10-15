
from collections import deque

def demo():
  # dq = deque(range(10), maxlen=10)
  dq = deque(range(10))

  print(dq)
  # dq.rotate(3)
  # print(dq)
  dq.rotate(-3)
  print(dq)
  print(dq[0])
  dq.appendleft(-1)
  print(dq)
  dq.extend([11, 22, 33])
  print((dq))
  dq.extendleft([110, 220, 330])
  print((dq))


if __name__ == '__main__':
  demo()
