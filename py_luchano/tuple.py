from collections import namedtuple

def coll_namedtuple():
  City = namedtuple('City', 'name country population coordinates')
  tokyo = City('Tokyo', 'JP', population=36.99, coordinates=(35.66, 139.69))
  print(tokyo)
  print(City._fields)

  LatLong = namedtuple('LatLong', 'lat long')
  delhi_data =('Delhi NCR', 'IN', 21.935, LatLong(28.61, 77.20))
  delhi = City._make(delhi_data)
  print(delhi._asdict())

def list_of_lists():
  a = [['a', 'b']]
  b = a * 5
  print(b)

  a[0][0] = 'c'
  print(b) 

  b[0][1] = 'd'

  print('\n')
  print(a)
  print(b)


if __name__ == '__main__':
  # coll_namedtuple()
  list_of_lists()
