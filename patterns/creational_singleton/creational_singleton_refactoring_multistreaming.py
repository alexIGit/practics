from __future__ import annotations
from threading import Lock, Thread
from typing import Optional


class SingletonMeta(type):
  _instance: Optional[Singleton] = None

  _lock: Lock = Lock()

  def __call__(cls, *args, **kwargs):
    with cls._lock:
      if not cls._instance:
        cls._instance = super().__call__(*args, **kwargs)

    return cls._instance


class Singleton(metaclass=SingletonMeta):
  value = None

  def __init__(self, value):
    self.value = value

  def some_business_logic(self):
    pass

def test_singleton(value, *args, **kwargs):
  singleton = Singleton(value)
  print(singleton.value)


if __name__ == "__main__":
  print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

  process1 = Thread(target=test_singleton, args=('FOO',))
  process2 = Thread(target=test_singleton, args=('BAR',))

  process1.start()
  process2.start()


