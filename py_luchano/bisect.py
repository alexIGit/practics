import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FTM = '{0:2d} @ {1:2d}, {2}{0:>2d}'

def demo(bisect_fn):
  for needle in reversed(NEEDLES):
    position = bisect_fn(HAYSTACK, needle)
    offset = position * ' |'
    print(ROW_FTM.format(needle, position, offset))

def demo_insort():
  SIZE = 7
  random.seed(1729)

  my_list = []
  for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

if __name__ == '__main__':
  # if sys.argv[-1] == 'left':
  #   bisect_fn = bisect.bisect_left
  # else:
  #   bisect_fn = bisect.bisect
  #
  # print('DEMO:', bisect_fn.__name__)
  # print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
  # demo(bisect_fn)

  demo_insort()


