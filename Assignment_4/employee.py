# Create an abstract class Employee with an abstract method calculate_salary(). Create subclasses Intern, FullTimeEmployee & ContractEmployee that implement the method differently. 
from abc import ABC, abstractmethod

class Employee(ABC):
  @abstractmethod
  def calculate_salary(self):
    pass
  
class Intern(Employee):
  def calculate_salary(self):
    return 10_000

class FullTimeEmployee(Employee):
  def calculate_salary(self):
    return 50_000

class ContractEmployee(Employee):
  def calculate_salary(self):
    return 30_000  
  
emp1 = Intern()
emp2 = FullTimeEmployee()
emp3 = ContractEmployee()

print("Intern salary:", emp1.calculate_salary())
print("FullTime salary:", emp2.calculate_salary())
print("Contract salary:", emp3.calculate_salary())  