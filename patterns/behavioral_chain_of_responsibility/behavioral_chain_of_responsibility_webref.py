
class Account():
	incomer = {}
	# def __init__(self):
	# 	self.incomer = {}

	def pay(self, order_price):
		is_can_pay = self.can_pay(order_price)
		if is_can_pay:
			print(f"Paid {order_price} using {self.name}")
		elif self.incomer:
			print(f"cannot pay using {self.name}")
			self.incomer.pay(order_price)
		else:
			print("Unfortunately, not enought money")



	def can_pay(self, amount):
		is_enough_many = self.balance >= amount
		# print(is_enough_many)
		return is_enough_many

	def set_next(self, account):
		self.incomer = account

	def __str__(self):
		return self.name

	def show(self):
 		# incomer ='none'
 		incomer = self.incomer

 		# if self['incomer']:
 		# 	incomer = self.incomer

 		print(f"""name: {self.name} \t-> balance: {self.balance} \t-> incomer: {incomer}""")


class Master(Account):
	def __init__(self, balance):
		super()
		self.name = 'Master Card'
		self.balance = balance


class Paypal(Account):
	def __init__(self, balance):
		super()
		self.name = 'Paypal'
		self.balance = balance


class Qiwi(Account):
	def __init__(self, balance):
		super()
		self.name = 'Qiwi'
		self.balance = balance

if __name__ == "__main__":
	master = Master(100)
	paypal = Paypal(200)
	qiwi = Qiwi(500)

	master.set_next(paypal)
	paypal.set_next(qiwi)

	master.pay(500)
	master.show()
	paypal.show()
	qiwi.show()