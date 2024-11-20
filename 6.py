class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}  # Dictionary to store subject-wise marks

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        print(f"Added/Updated marks for {self.name}: {subject} = {marks}")

    def show_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")


class School:
    def __init__(self):
        self.students = []  # List to store Student objects

    def add_student(self, student):
        for existing_student in self.students:
            if existing_student.roll_no == student.roll_no:
                print(f"Student with Roll No {student.roll_no} already exists.")
                return
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student with Roll No {roll_no} removed successfully!")
                return
        print(f"Student with Roll No {roll_no} not found.")

    def show_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("\n--- All Students ---")
            for student in self.students:
                student.show_details()

    def find_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n--- Student Found ---")
                student.show_details()
                return
        print(f"Student with Roll No {roll_no} not found.")


# Main Program
if __name__ == "__main__":
    school = School()

    # Adding initial students
    student1 = Student("Alice", 1)
    student1.add_marks("Math", 90)
    student1.add_marks("Science", 85)

    student2 = Student("Bob", 2)
    student2.add_marks("Math", 75)
    student2.add_marks("History", 80)

    school.add_student(student1)
    school.add_student(student2)

    # Display all students
    school.show_all_students()

    # Add marks for an existing student
    print("\nAdding marks for Bob...")
    school.find_student(2)
    student2.add_marks("Science", 70)

    # Remove a student
    print("\nRemoving student with Roll No 1...")
    school.remove_student(1)

    # Display all students again
    school.show_all_students()

    # Try to find a removed student
    print("\nSearching for a removed student...")
    school.find_student(1)
