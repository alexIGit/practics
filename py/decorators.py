
#  @property
class Person:
	name = 'David'
	lastname = "Pytin"

	@property
	def fullname(self):
		print(f"{self.name} {self.lastname}")

	def get_fulname(self):
		print(f"{self.name} {self.lastname}")		
	



def check_property():
	person = Person()

	person.fullname
	person.get_fulname()


# 





if __name__ == "__main__":
	check_property()
