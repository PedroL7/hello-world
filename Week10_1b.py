class Student():
    def __init__(self, surname, firstname, numbers, course):
        self.surname = surname
        self.firstname = firstname
        self.numbers = numbers
        self.course = course

    def show_studentdetails(self):
        print("\nList of student information")
        print("Surname: ", self.surname, "\nFirst name: ", self.firstname, "\nStudent number: ", self.numbers, "\nCourse: ", self.course)
        

    def new_firstname_surname(self, new_firstname, new_surname):
        self.surname = new_surname
        self.firstname = new_firstname
    
