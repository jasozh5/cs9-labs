from Animal import Animal 

class AnimalShelter:

    def __init__(self):
        self.dict = {}

    def addAnimal(self, animal):
        a = 0
        if animal.species in self.dict:
            p = self.dict[animal.species]
            p.append(animal)
            self.dict[animal.species] = p
        else:
            self.dict[animal.species] = [animal]

    def removeAnimal(self, animal):
        for x in self.dict:
            if x == animal.species:
                a = -1
                for y in self.dict[x]:
                    a = a+1
                    if y.name == animal.name and y.weight == animal.weight and y.age == animal.age:
                        self.dict[x].pop(a)

    def removeSpecies(self, species):
        for x in self.dict:
            if x == species.upper():
                self.dict.pop(x)
                break

    def getAnimalsBySpecies(self, species):
        for x in self.dict:
            if x == species.upper():
                v = ''
                for y in self.dict[x]:
                    v = v+y.toString()+'\n'
                return v[0:len(v)-1]

    def doesAnimalExist(self, animal):
        for x in self.dict:
            if x == animal.species:
                for y in self.dict[x]:
                    if y.weight == animal.weight and y.age == animal.age and y.name == animal.name:
                        return True

        return False
