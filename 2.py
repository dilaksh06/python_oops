class student:
    def __init__(self,name):
        self.name=name

no=int(input("enter the number of students : "))

std=[]

for x in range (no):
    name=input(f"enter the nmae of the {x+1} student : ")
    std.append(name)
    
students=student(std)
print(students.name)
    
    
