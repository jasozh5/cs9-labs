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
                    
                
                    

    
bear1 = Animal('bear', 69, 123, "Dave")
bear2 = Animal('bear', 123, 123131, 'John')
horse1 = Animal('horse', 78, 232, 'Horsey')
horse2 = Animal('horse', 21, 12, 'Ally')
horse3 = Animal('horse', 12, 23, 'Johnny')
cat1 = Animal('cat', 123 ,23, 'Kitty')

d = AnimalShelter()
d.addAnimal(bear1)
d.addAnimal(bear2)
d.addAnimal(horse1)
d.addAnimal(horse2)
print(d.dict)

print(d.getAnimalsBySpecies('horse'))

print(d.doesAnimalExist(horse2))

print(d.doesAnimalExist(cat1))
print(d.doesAnimalExist(horse3))



