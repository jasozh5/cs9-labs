class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.species = species.upper()
        self.age = age
        self.weight = weight
        self.name = name.upper()

    def setSpecies(self, species):
        self.species = species.upper()

    def setName(self, name):
        self.name = name.upper()

    def setWeight(self,weight):
        self.weight = weight

    def setAge(self,age):
        self.age = age

    def toString(self):
        return "Species: {}, Name: {}, Age: {}, Weight: {}"\
               .format(self.species, self.name, self.age, self.weight)
