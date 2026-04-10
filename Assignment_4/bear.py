class Herbivore:
  def eat_plants(self):
    print("Eating plants and fruits")


class Carnivore:
  def eat_meat(self):
    print("Eating meat")


class Omnivore:
  def eat_both(self):
    print("Eating plants AND meat.")


class Bear(Herbivore, Carnivore, Omnivore):
  def __init__(self, name, color):
        self.name = name
        self.color = color

  def display(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        self.eat_plants()
        self.eat_meat()
        self.eat_both()


b1 = Bear("Baloo", "Brown")
b1.display()
