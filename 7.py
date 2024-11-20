class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        return(f"the name is {self.name} and age is {self.age}")

person1=person("dilakshan",26)
person2=person("ABC",23)
person3=person("daughter",4)
person_list=[person1,person2,person3]

for x in person_list:
    print(x.show_details())
