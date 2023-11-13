"""version: python 3.8"""
"""оператор присваивания :="""
import re

hello = "Hello, Vasja!"

# old
name = re.search(r', (.*)!', hello)
if name:
  print(name.group(1))

#new
if (name1 := re.search(r', (.*)!', hello)):
  print(name1.group(1))

"""строго позиционные аргументы   / """
def some_func(x, y, /):
  print(x, y)

#worked version
some_func(1, 2)

#failed version
try:
  some_func(x=1, y=2)
except:
  print("No working: some_func(x=1, y=2)")

"""Изменения f-string"""
name = "Vasja"
#old
print(f'{name}')
print(f'name={name}')
#new
print(f'{name=}')

"""Новые типы в typing"""
# from typing import TypedDict
# from typing_extensions import TypedDict
# class Client(TypedDict):
#   id: int
#   name: str
#
# client = Client(id=1, name='Vasja')

"""Получение версии библиотек в рантайме">Получение версии библиотек в рантайме<"""
# from importlib.metadata import version
# print(version('Django'))

"""version: python 3.9"""
"""Объеденение словарей"""

dict1 = {'a':1, 'c': 1}
dict2 = {'b':2, 'c': 2}
# var: 1
dict3 = {**dict1, **dict2}
print(dict3)
# var: 2
dict4 = dict1 | dict2
print(dict4)

dict5 = {}
dict5 |= dict4
print(dict5)

"""type hinting"""
# вместо:
# from typing import Dict
# def print_phone_book(book: Dict[str, str]) -> None:
# ->
def print_phone_book(book: dict[str, str]) -> None:
  for name, phone in book.items():
    print(f'{name.ljust(12)} - {phone}')

book = {
  "Крыша горит": "01",
  "Крыша нужна": "02"
}
print_phone_book(book)

"""Удаление префиксов и суффиксов в строках"""
#old
def string_quotes(text):
  if text.startswith('"'):
    text = text[1:]
  if text.endswith('"'):
    text = text[:-1]
  print(text)
  return text
string_quotes('"frefrefe"')

#new
text = '"frefrefe"'
text1 = text.removeprefix('"')
text2 = text.removesuffix('"')
print(f'{text1=} - {text2=}')
