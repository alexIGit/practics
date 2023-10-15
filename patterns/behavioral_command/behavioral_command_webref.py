class Driver:
	def __init__(self, command):
		self.command = command

	def execute(self):
		self.command.execute()



class Engine:
	def __init__(self):
		self.state = False 

	def on(self):
		self.state = True

	def off(self):
		self.state = False

	def info(self):
		print(f"state is: {self.state}")


class On_Start_Command:
	def __init__(self, engine):
		self.engine = engine

	def execute(self):
		self.engine.on()


class On_Switch_Off_Command:
	def __init__(self, engine):
		self.engine = engine

	def execute(self):
		self.engine.off()


if __name__ == "__main__":
	engine = Engine()

	engine.info()

	on_start_command = On_Start_Command(engine)
	driver = Driver(on_start_command)
	driver.execute()

	engine.info()
