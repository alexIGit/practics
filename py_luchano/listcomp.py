
from service.dec_print_func_name import print_func_name

@print_func_name
def listcomp_v1(symbols):
  codes = []

  for symbol in symbols:
    codes.append((ord(symbol)))

  print(codes)

@print_func_name
def listcomp_v2(symbols):
  codes = [ord(symbol) for symbol in symbols]
  print(codes)

@print_func_name
def gencomp_v1(symbols):
  codes = tuple(ord(symbol) for symbol in symbols)
  print(codes)


@print_func_name
def listcomp_v3(symbols):
  codes = [ord(s) for s in symbols if ord(s) > 40]
  print(codes)

@print_func_name
def gencomp_v1(symbols):
  codes = tuple(ord(symbol) for symbol in symbols)
  print(codes)

@print_func_name
def gencomp_v2(symbols):
  import array
  codes = array.array('I', (ord(symbol) for symbol in symbols))
  print(codes)

@print_func_name
def list_map_filter(symbols):
  codes = list(filter(lambda c: c > 40, map(ord, symbols)))
  print(codes)

@print_func_name
def multiple_decart(data):
  colors = data.get('colors')
  sizes = data.get('sizes')

  tshirts = [(color, size) for color in colors for size in sizes]
  print(tshirts)

@print_func_name
def multiple_decart_v2(data):
  colors = data.get('colors')
  sizes = data.get('sizes')

  tshirts = [(color, size) for size in sizes for color in colors]
  print(tshirts)

@print_func_name
def multiple_decart_gencomp(data):
  colors = data.get('colors')
  sizes = data.get('sizes')

  for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

@print_func_name
def multiple_decart_v3(data):
  colors = data.get('colors')
  sizes = data.get('sizes')

  for color in colors:
    for size in sizes:
      print((color, size))

if __name__ == '__main__':
  symbols = '$&^%$'

  # listcomp_v1(symbols)
  # listcomp_v2(symbols)
  # gencomp_v1(symbols)
  # gencomp_v2(symbols)

  # listcomp_v3(symbols)
  # list_map_filter(symbols)

  multiple_decart_data = {
    'colors': ['black', 'white'],
    'sizes': ['S', 'M', 'L']
  }

  multiple_decart(multiple_decart_data)
  multiple_decart_v2(multiple_decart_data)
  multiple_decart_v3(multiple_decart_data)
  multiple_decart_gencomp(multiple_decart_data)

