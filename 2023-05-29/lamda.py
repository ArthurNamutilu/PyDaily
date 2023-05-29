people = [
	{'name': 'Arthur', 'school': 'computing'},
	{'name': 'James', 'school': 'business'},
	{'name': 'Kevin', 'school': 'education'}
]

people.sort(key = lambda person: person['school'])
print(people)
