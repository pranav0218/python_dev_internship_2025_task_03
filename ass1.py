class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total = self.calculate_total()
        percentage = (total / (len(self.marks) * 100)) * 100
        return percentage

    def assign_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 75:
            return "Distinction"
        elif percentage >= 60:
            return "First Class"
        elif percentage >= 50:
            return "Second Class"
        else:
            return "Fail"

    def display_details(self):
        print("\nStudent Details")
        print(f"ID         : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Marks      : {self.marks}")
        print(f"Total      : {self.calculate_total()}")
        print(f"Percentage : {self.calculate_percentage():.2f}%")
        print(f"Grade      : {self.assign_grade()}")

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))
    for j in range(subjects):
        mark = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    student = Student(student_id, name, marks)
    students.append(student)

for student in students:
    student.display_details()
