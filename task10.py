# Statement: A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

# Age is greater than 20
# Marks is between 0 and 100 (both inclusive)
# A student qualifies for admission, if

# Age and marks are valid and
# Marks is 65 or more
# Write a python program to represent the students seeking admission in the university. The details of student class are given below.

class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_marks() and self.__age > 20:
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False

    # Setter methods
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age


# Example usage:
if __name__ == "__main__":
    # Create a student object
    student1 = Student()

    # Set student details
    student1.set_student_id("S001")
    student1.set_marks(70)
    student1.set_age(22)

    # Check qualification
    if student1.check_qualification():
        print("Student qualifies for admission")
    else:
        print("Student does not qualify for admission")
