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
