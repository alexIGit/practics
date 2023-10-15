class OfficialDealer:
 	customers = []

 	def addToCustomersList(self, name):
 		self.customers.append(name)

 	def orderAuto(self, customer, auto, info):
 		name = customer.getName()
 		print(f"Order name: {name}. order auto is {auto}")
 		print(f"Additional info: {info}")
 		self.addToCustomersList(name)

 	def get_customers_list(self):
 		print(self.customers)





class Customer:
	def __init__(self, name, dealerMediator):
		self.name = name
		self.dealerMediator = dealerMediator

	def getName(self):
		return self.name

	def make_order(self, auto, info):
		self.dealerMediator.orderAuto(self, auto, info)




if __name__ == "__main__":
	mediator = OfficialDealer()
	cust1 = Customer('name1', mediator)
	cust2 = Customer('name2', mediator)

	cust1.make_order('tesla', '+autopilot')
	cust2.make_order('bmw', '+parktronik')

	mediator.get_customers_list()