# Create a class Student with private attributes: name, roll number & marks. Provide getter & setter methods with validation (eg: marks cannot be negative, roll number has to be between 1 & 100). A name cannot be empty.
class Student:
  def __init__(self, name, roll_no, marks):
    self.__name = name
    self.__roll_no = roll_no
    self.__marks = marks
    
  def get_name(self):
    return self.__name
    
  def get_roll_no(self):
    return self.__roll_no
    
  def get_marks(self):
    return self.__marks
     
  def set_name(self, name):
    if name and name.strip(): 
      self.__name = name.strip()
    else:
      print("Name cannot be empty!")
      
  def set_roll_no(self, roll_no):
    if 1 <= roll_no <= 100:
      self.__roll_no = roll_no
    else:
      print("Roll number must be 1-100!")
    
  def set_marks(self, marks):
    if marks >= 0:
      self.__marks = marks
    else:
      print("Marks cannot be negative!") 
      
          
  def display(self):
    print(f"Name: {self.__name}, Roll: {self.__roll_no}, Marks: {self.__marks}")

s1 = Student("Aman", 25, 85)
s1.display() 

s1.set_name(" ")
s1.set_marks(-8)
s1.set_roll_no(101)
       
    