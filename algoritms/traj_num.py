"""
  Kлассический набор программок для одномерного динамического программирования.
"""

def count_trajectories(number):
  """
    Задачи о кузнечике (количество траекторий, траектория наименьшей стоимости).
    Прыгает вперед на +1 и +2.
    Сколько различных траекторий допрыгать из 1 в N.
  """

  count_tracks = [0, 1] + [0] * number

  for i in range(2, number + 1):
    count_tracks[i] = count_tracks[i - 2] + count_tracks[i - 1]

  return count_tracks[number]


def count_trajectories_improved(number, allowed:list):
  """
    Запретим некоторые клетки.
    Прыгает вперед на +1, +2 и +3
  """

  trajectories = [0, 1, int(allowed[2])] + [0] * (number - 2)

  for i in range(3, number + 1):
    if allowed[i]:
      trajectories[i] = trajectories[i - 1] + trajectories[i - 2] + trajectories[i - 3]

  return trajectories[i]


def count_min_cost(num, price:list):
  """
    Минимальная стоимость достижения клетки num.
    Прыгает вперед на +1 и +2.
    price[i] - цена за посещение клетки i;
    cost[i] - минимальная стоимость достижения клетки i;

    формула:
    cost[i] = price[i] + min(cost[i-2], cost[i-1])
    cost[1] = price[1]
    cost[2] = price[1] + price[2]
  """

  # float("-inf") - минус бесконечность

  cost = [float("-inf"), price[1], price[1] + price[2]] + [0] * (num - 2)

  for i in range(3, num + 1):
    cost[i] = price[i] + min(cost[i - 1], cost[i - 2])

  return cost(num)





if __name__ == "__main__":
  tracks = count_trajectories(10)

  allowed_cells = [True] * 13

  tracks_improved = count_trajectories_improved(10, allowed_cells)



  print(tracks)
  print(tracks_improved)

  print()
