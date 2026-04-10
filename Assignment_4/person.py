class Person:
  def __init__(self, name, age=None, address=None):
    self.name = name
    self.age = age
    self.address = address
    
  def display(self):
    print(f"Name: {self.name}")
    if self.age:
      print(f"Age: {self.age}")
    if self.address:
      print(f"Address: {self.address}")


p1 = Person("Aman")                    
p2 = Person("Priya", 25)               
p3 = Person("Rahul", 30, "Delhi")      

print("Person 1")
p1.display()
print("\nPerson 2")
p2.display()
print("\nPerson 3")
p3.display()