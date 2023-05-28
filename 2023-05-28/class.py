class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def person_info(self):
		print(f"Name: {self.name} age is: {self.age}")


Gg = Person("Fred", 23)
Gg.person_info()
