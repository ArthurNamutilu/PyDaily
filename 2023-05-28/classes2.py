class Flight:
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []

	def available_seats(self):
		return self.capacity - len(self.passengers)

	def add_passenger(self, name):
		if not self.available_seats():   # same as available_seats == 0
			return False
		self.passengers.append(name)
		return True

fly540 = Flight(3)
people = ["Arthur", "Gg", "Fred", "Dela"]

for person in people:
	if fly540.add_passenger(person):
		print(f'{person} successfully added to flight')
	else:
		print(f'No available seats for {person}')


print(f"on board {fly540.passengers}")
