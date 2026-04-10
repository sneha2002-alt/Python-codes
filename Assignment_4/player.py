class Player:
  player_count = 0
  def __init__(self, name, level):
    self.name = name
    self.level = level
    Player.player_count +=1
    
  def display(self):
    print(f"Player: {self.name}, Level: {self.level}")
    
p1 = Player("Aman", 5)
p1.display()

p2 = Player("Priya", 3)
p2.display()

p3 = Player("Rahul", 9)
p3.display()    

print(f"Total Players: {Player.player_count}")   

