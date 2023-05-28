class Circle:
	pi = 3.14159

	def __init__(self, radius):
		self.radius = radius


	def calc_area(self):
		return self.pi * (self.radius ** 2)


	@classmethod
	def update_pi(cls, new_pi):
		cls.pi = new_pi
