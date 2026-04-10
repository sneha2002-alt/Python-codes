class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    
  def display(self):
    print(f"{self.brand} {self.model}")

class Car(Vehicle):
  def __init__(self, brand, model, seats):
    super().__init__(brand, model)
    self.seats = seats
    
  def display(self):
    print(f"{self.brand} {self.model} - Seats: {self.seats}")

class Bike(Vehicle):
  def __init__(self, brand, model, engine_cc):
    super().__init__(brand, model)
    self.engine_cc = engine_cc
    
  def display(self):
    print(f"{self.brand} {self.model} - Engine: {self.engine_cc}cc")


car1 = Car("Toyota", "Camry", 5)
bike1 = Bike("Yamaha", "R15", 155)

car1.display()
bike1.display()