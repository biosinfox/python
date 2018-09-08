class Plant:

    plants=0

    leaves_count=2

    def __init__(self,name,variety):
        self.name=name
        self.variety=variety
        #Increment the number of plants every time when a new instance of plant is created.
        Plant.plants+=1 

    def plantData(self):
        return '{} {}'.format(self.name,self.variety)

print(Plant.plants)
orange=Plant('Orange','Green Variety')
print(Plant.plants)
banana=Plant('Matooke','Muvubo')
print(Plant.plants)
print(banana.plantData())
print(orange.plantData())

print(banana.__dict__)
print(Plant.__dict__)
