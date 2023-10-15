 
class Auto:
	def accept(self, visitor):
		return visitor(self)


class Tesla(Auto):
	def info(self):
		# print('It is a Tesla car!')
		return 'It is a Tesla car!'

class Bmw(Auto):
	def info(self):
		# print('It is a BMW car!')
		return 'It is a BMW car!'


def export_visitor(auto):
	if isinstance(auto, Tesla):
		return (f"Exported data for Tesla: {auto.info()}")

	if isinstance(auto, Bmw):
		return (f"Exported data for Bmw: {auto.info()}")



if __name__ == "__main__":
	tesla = Tesla()
	bmw = Bmw()



	print(tesla.accept(export_visitor))
	print(bmw.accept(export_visitor))