
class AutoNews:
	news = '' 
	actions = []

	def set_news(self, text):
		self.news = text
		self.notify_all()

	def notify_all(self):

		# def inform(user):
		# 	user.inform(self)

		# list(map(inform, self.actions))

		list(map(lambda x: x.inform(self), self.actions))


	def register(self, observer):
		self.actions.append(observer)

	# def unregister(observer):





class Jack:
	def inform(self, message):
		print(f"Jack has been informed about: {message.news}")

	def __str__(self):
		return 'Jack'

class Max:
	def inform(self, message):
		print(f"Max has been informed about: {message.news}")

	def __str__(self):
		return 'Max'		


if __name__ == "__main__":
	auto_news = AutoNews()
	auto_news.register(Jack())
	auto_news.register(Max())

	auto_news.set_news("New Tesla prise is 40 000")