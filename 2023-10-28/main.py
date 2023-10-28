class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.age = breed

    def barks(self):
        print(f'{self.name} barks!')


dog1 = Dog("Bosco", 'Golden Retriever')    # dog1 == object
dog1.barks()