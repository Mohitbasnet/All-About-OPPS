
# Q-5: Problem 5 based on OOP Python.
# TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

# eligibility criteria:
# if experience is more than 3 years, average feedback should be 4.5 or more
# if experience is 3 years or less, average feedback should be 4 or more
# he/she should posses the technology skill for the course
# Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

# Note:

# Consider all instance variables to be private and methods to be public.
# An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
# check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
# allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
# Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.


class Instructor:
    def __init__(self, name, experience, feedback, technology_skills):
        self.__name = name
        self.__experience = experience
        self.__feedback = feedback
        self.__technology_skills = technology_skills

    def set_experience(self, experience):
        self.__experience = experience

    def set_feedback(self, feedback):
        self.__feedback = feedback

    def set_technology_skills(self, technology_skills):
        self.__technology_skills = technology_skills

    def check_eligibility(self):
        if self.__experience > 3:
            return self.__feedback >= 4.5
        else:
            return self.__feedback >= 4

    def allocate_course(self, required_technology):
        return required_technology in self.__technology_skills

# Testing the class
instructor1 = Instructor("Mohit Basnet", 5, 4.8, ["Python", "Java", "C++"])
instructor2 = Instructor("Suman giri", 2, 4.2, ["JavaScript", "HTML", "CSS"])

print("Instructor 1 Eligibility:", instructor1.check_eligibility())  # True
print("Instructor 1 Course Allocation:", instructor1.allocate_course("Python"))  # True
print("Instructor 1 Course Allocation:", instructor1.allocate_course("JavaScript"))  # False

print("Instructor 2 Eligibility:", instructor2.check_eligibility())  # True
print("Instructor 2 Course Allocation:", instructor2.allocate_course("JavaScript"))  # True
print("Instructor 2 Course Allocation:", instructor2.allocate_course("Python"))  # False
