class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


book1 = book("451 градусов по фаренгейту", "Рэй Брэдбери", "1953")

print(book1.get_info())