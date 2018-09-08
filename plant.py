class Plant:

    plants=0

    leaves_count=2

    def __init__(self,name,variety,color):
        self.name=name
        self.variety=variety
        self.color=color
        #Increment the number of plants every time when a new instance of plant is created.
        Plant.plants+=1 

    def data(self):
        return '{} {} {}'.format(self.name,self.variety,self.color)
    @classmethod
    def from_string(cls,plant_str):
        name,variety,color=plant_str.split('-')
        return cls(name,variety,color)

print(Plant.plants)
orange=Plant('Orange','Green Variety','Orange')
print(Plant.plants)
banana=Plant('Matooke','Muvubo','Green')
print(Plant.plants)
print(banana.data())
print(orange.data())

print(banana.__dict__)
print(Plant.__dict__)

plant_a='Apple-Green-Green'
print(Plant.plants)
plant_p='Pear-Green-Green'
print(Plant.plants)
plant_g='Grapes-Purple-Purple'
print(Plant.plants)

name,variety,color=plant_a.split('-')
apple=Plant(name,variety,color)
name,variety,color=plant_p.split('-')
pear=Plant(name,variety,color)
name,variety,color=plant_g.split('-')
grapes=Plant(name,variety,color)

print(apple.data())
print(pear.data())
print(grapes.data())

plant_str_1='Melon-Yellow-Yellow'
plantB=Plant.from_string(plant_str_1)
print(plantB.data())



class Apple(Plant):
    def __init__(self,name,variety,color,leaves):
        super().__init__(name,variety,color)
        self.leaves=leaves


apple1=Apple('Apple Pink','Pink Variety','Pink Color')
print(apple1.data())


