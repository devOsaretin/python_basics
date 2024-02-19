class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages


my_book = Book('Chase', 'Osaretin', 120)

print(my_book)
print(len(my_book))