class student:
    def __init__(self,name=None):
        self.name=[]
    def add_name(self,names):
        self.name.append(names);
        return self.name


no=int(input("enter the number of students : "))
students=student()
for x in range (no):
    name=input(f"enter the nmae of the {x+1} student : ")
    
    students.add_name(name)
print(students.name)
