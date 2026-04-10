class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.reviews = []
    
    
  def add_review(self, review):
    self.reviews.append(review)
    print(f"Review added for '{self.title}'")
    
  def count_reviews(self):
    return len(self.reviews)
  
  def display_reviews(self):
    print(f"\n{self.title} by {self.author}")
    print(f"Total Reviews: {self.count_reviews()}") 
     
    for i, review in enumerate(self.reviews, 1):
        print(f"{i}. {review}")

book1 = Book("Python Crash Course", "Eric Matthes")

book1.add_review("Excellent for beginners! Clear examples.")
book1.add_review("Good book but needs more advanced topics")
book1.add_review("Best Python book I've read so far!")

book1.display_reviews()
      