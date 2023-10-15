import random

def flip():
	if random.randrange(0, 2) == 0:
		print('Heads')
	else:
		print("Tails")


def divisorpatter(num):
	
	for i in range(1, num + 1):

		for j in range(1, num + 1):
			
			if (i % j == 0) or (j % i == 0):
				print(' * ', end='')
			else:
				print('   ', end='')

		print(i)

def gambler(stake, goal, trials):
	"""Monte-Carlo
	  :param: stake - начальная сумма 
	  :param: goal - цель
	  :param: trials - количество попыток
	  :param: bets - счётчик ставок
	  :param: wins - счётчик выигрышей
	  :param: cash -  наличность
	"""

	bets = 0
	wins = 0

	for t in range(trials):
		# запуск одной попытки
		cash = stake

		while cash > 0 and cash < goal:
			# модель одной ставки
			bets += 1

			if random.randrange(0, 2) == 0:
				cash += 1
			else:
				cash -= 1

		if cash == goal:
			wins += 1

	print(str(100 * wins // trials) + '% wins')
	print('Avg # bets: ' + str(bets // trials))



if __name__ == "__main__":
	# flip()
	# divisorpatter(16)
	gambler(10, 20, 1000)
	gambler(50, 250, 100)
	# gambler(500, 2500, 100)
