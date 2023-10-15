import collections

def demo():
  a = dict(one=1, two=2)
  b = {'one': 1, 'two': 2}
  c = dict(zip(['one', 'two'], [1, 2]))
  d = dict({'two': 2, 'one': 1})
  e = dict([('one', 1), ('two', 2)])

  print(e)

  print(a == b == c == d == e)

def dictcomp():
  '''Словарное включение'''
  DIAL_CODES = [
    (86, 'China'),
    (91, 'India')
  ]

  country_code = {country: code for code, country in DIAL_CODES}
  print(country_code)

  country_code_up = {code: counrty.upper() for counrty, code in country_code.items() if code < 90}
  print(country_code_up)

def todo_collections():
  ct = collections.Counter('aaaaadd')
  print(ct)

  ct.update('aaaaadddzzz')
  print(ct)

  most = ct.most_common(2)
  print(most)


class StrKeyDict(collections.UserDict):
  def __missing__(self, key):
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]

  def __contains__(self, key):
    return str(key) in self.data

  def __setitem__(self, key, item):
    self.data[str(key)] = item

def userdict():
  pass

####
def mapping_proxy_types():
  from types import MappingProxyType

  d = {1: 'A'}
  d_proxy = MappingProxyType(d)
  print(d_proxy)

  try:
    d_proxy[2] = 'x' # вызовет ошибку
  except TypeError as err:
    print(err)

  d[2] = 'B'
  print(d_proxy)

if __name__ == '__main__':
  # demo()
  # dictcomp()
  # todo_collections()
  mapping_proxy_types()
