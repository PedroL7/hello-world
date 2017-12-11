class Student():
    def __init__(self, surname, firstname, numbers, course):
        self.surname = surname
        self.firstname = firstname
        self.numbers = numbers
        self.course = course

    def show_studentdetails(self):
        print("\nList of student information")
        print("Surname: ", self.surname, "\nFirst name: ", self.firstname, "\nStudent number: ", self.numbers, "\nCourse: ", self.course)
        

def main():
    surname = input("Please enter your surname:")
    firstname = input("Please enter your name:")
    numbers = input("Please enter your student number:")
    course = input("Please enter your course:")

    student = Student(surname, firstname, numbers, course)
    student.show_studentdetails()
main()
