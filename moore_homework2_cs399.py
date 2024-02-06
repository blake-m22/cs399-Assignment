# Blake Moore HW2 OOP 
# CS399 Dr.Paulis
# This program creates Student classes and the undergrad and postgrad classes inherit from the student class
 

class Student: #creats the new student class and intitalizes its attributeds
        """
    A class representing a student.

    Attributes:
        student_ID (int): The unique identifier for the student.
        name (str): The name of the student.
        marks (str): The academic marks of the student.
    """
        def __init__(self, student_ID: int, name: str, marks: str) -> None:
                self.student_ID = student_ID
                self.name = name
                self.marks = marks
        def __str__(self) -> str:
                return f"Student: {self.name}, ID: {self.student_ID}, Marks: {self.marks}"  


class undergraduate(Student): #intitalizes the undergraduate class and intitalizes its attributes
        """
    A class representing an undergraduate student, inheriting from the Student class.

    Attributes:
        sat_score (int): The SAT score of the undergraduate student.
        student_ID (int): The unique identifier for the student.
        name (str): The name of the student.
        marks (str): The academic marks of the student.
    """

        def __init__(self,sat_score: int, student_ID: int, name: str, marks: str) -> None:
             super().__init__(student_ID, name, marks)
             self.sat_score = sat_score
        def __str__(self) -> str: 
           return f"Undergraduate: {self.name}, ID: {self.student_ID}, Marks: {self.marks}, SAT Score: {self.sat_score}"  

class Postgraduate(undergraduate): 
        """
    A class representing a postgraduate student, inheriting from the undergraduate class.

    Attributes:
        bachelors_gpa (int): The GPA of the postgraduate student's bachelor's degree.
        student_ID (int): The unique identifier for the student.
        name (str): The name of the student.
        marks (str): The academic marks of the student.
        sat_score (int): The SAT score of the student.
    """
        def __init__(self, bachelors_gpa: int, student_ID: int, name: str, marks: str, sat_score: int) -> None:
                super().__init__(student_ID, name, marks, sat_score)
                self.bachelors_gpa = bachelors_gpa
        def __str__(self): 
              return f"Postgraduate: {self.name}, ID: {self.student_ID}, Marks: {self.marks}, SAT Score: {self.sat_score}, Bachelors GPA: {self.bachelors_gpa}"  


Mark = undergraduate(1500, 12345, "Mark Smith", "A") 
print(Mark)
Blake = Postgraduate(3.8, 1330, 12346,"Blake Moore", "B")
print(Blake)
Drew = Student(12347, "Drew Barry","C")
print(Drew)
students_list = [Blake, Mark, Drew] #This is a list of students

for student in students_list: #this goes through the list of students and prints out their first name
       print(student.name)