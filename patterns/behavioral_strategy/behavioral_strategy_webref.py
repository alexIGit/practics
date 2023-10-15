def base_strategy(amount):
	return amount 

def premium_strategy(amount):
	return amount * 0.85

def platinum_strategy(amount):
	return amount * 0.5

class AutoCart:
	def __init__(self, discount):
		self.discount = discount
		self.amount = 0

	def checkout(self):
		print(self.discount(self.amount))
		return self.discount(self.amount)

	def set_amount(self, amount):
		self.amount = amount


if __name__ == "__main__":
	base_customer = AutoCart(base_strategy)
	prem_customer = AutoCart(premium_strategy)
	plat_customer = AutoCart(platinum_strategy)

	base_customer.set_amount(1000)
	base_customer.checkout()

	prem_customer.set_amount(1000)
	prem_customer.checkout()

	plat_customer.set_amount(1000)
	plat_customer.checkout()
	