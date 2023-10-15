class Builder:
	def  collect_accessories(self):
		print("Collect based Accessories")

	def build(self):
		self.add_engine()
		self.install_classis()
		self.collect_accessories()

class TeslaBuilder(Builder):
	def add_engine(self):
		print('Add electronic Engine!')

	def install_classis(self):
		print("Install Tesla Cassis")

	def add_electronic(self):
		print("Tesla add electronicks")

	def  collect_accessories(self):
		print("Collect Tesla Accessories")


class BmwBuilder(Builder):
	def add_engine(self):
		print('Add BMW electronic Engine!')

	def install_classis(self):
		print("Install BMW Cassis")

	def add_electronic(self):
		print("BMW add electronicks")


if __name__ == "__main__":
	tesla_builder = TeslaBuilder()
	bmw_builder = BmwBuilder()

	tesla_builder.build()
	bmw_builder.build()