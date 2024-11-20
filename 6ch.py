class Student():
    def __init__(self):
        self.marks={}
        self.student=[]
    def show_details(self):
        for x in range(len(self.student)):
            print(x+1,". Name->",self.student[x][0],", Roll_No->",self.student[x][1],", Marks->",self.student[x][2])
class school(Student):
    def add_student(self,student):
        x=self.student
        x.append(student)

    def remove_student(self,roll_no):
        for x in range(self.student):
            if roll_no==self.student[x][1]:
                self.studentn.pop(x)
                
    def show_all_students(self):
        self.show_details()
    def find_student(self,roll_no):
        for x in range(self.student):
            if roll_no in self.student[x][1]:
                print(self.student[x])

x1=["dilakshan",45,{"maths":45}]
x2=["dilakshan",45,{"maths":4}]
std=school()
std.add_student(x1)
std.add_student(x2)
std.show_all_students()
