class Library:
    def __init__ (self, city:str, street:str, zip_code, open_hours, phone):
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone

    def __str__(self):
        return (f"Library address: {self.street}, {self.zip_code} {self.city}, "f"Open hours: {self.open_hours}, Phone: {self.phone}")

class Employee:
    def __init__ (self, first_name:str, last_name:str, hire_date, city:str, street:str, zip_code, open_hours, phone):
        self.first_name=first_name
        self.last_name=last_name
        self.hire_date=hire_date
        self.city=city
        self.street=street
        self.zip_code=zip_code
        self.open_hours=open_hours
        self.phone=phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}, "f"Hire date: {self.hire_date}, Phone: {self.phone}")

class Book:
    def __init__(self, library: Library, publication_date:str, author_name:str, author_surname:str, number_of_pages:int):
        self.library= library
        self.publication_date=publication_date
        self.author_name=author_name
        self.author_surname=author_surname
        self.number_of_pages=number_of_pages

    def __str__(self):
        return (f"Library: {self.library}, "
                f"Publication date: {self.publication_date}, "
                f"Author name: {self.author_name}, "
                f"Author surname: {self.author_surname}, "
                f"Number of pages: {self.number_of_pages}")

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee=employee
        self.student=student
        self.books=books
        self.order_date=order_date

    def __str__(self):
        books_str = "\n".join(str(book) for book in self.books)
        return (f"Order date: {self.order_date}\n"
                f"{self.employee}\n"
                f"Student: {self.student}\n"
                f"Books:\n{books_str}")

library1=Library("Katowice", "Bażantów", "00-001", "9:30-10:00", "509 800 435")
library2=Library("Wrocław", "Polska", "30-004", "10:00-10:30", "600 087 363")

employee1=Employee("Anna", "Nowak", "2003-02-24", "Katowice", "Bażantów", "00-002", "9:00-10:00", "800 090 232")
employee2=Employee("Adam", "Kowalski", "2020-05-15", "Warszawa", "Ziołowa", "00-002", "8:00-10:00", "900 045 678")
employee3 = Employee("Ewa", "Mazur", "2021-06-01", "1995-08-30","Warsaw", "Birch 3", "00-300", "500-300-300")

book1 = Book(library1, "1990-02-19", "Justyna", "Kowalczyk", 900 )
book2 =Book(library2, "2020-06-14", "Artur", "Braszcz", 200)
book3 =Book(library1, "1999-09-19", "Pola", "Grzybowa", 360)
book4 = Book(library2, "1890-07-12", "Bogusław", "Nowak", 100)
book5=Book(library1, "2010-01-01", "Andrzej", "Makowiec", 169)

student1 = "Piotr Zielinski"
student2 = "Maria Lewandowska"
student3 = "Tomasz Kaczmarek"

order1 = Order(employee1, student1, [book1, book2], "2024-01-10")
order2 = Order(employee2, student2, [book3, book4, book5], "2024-01-12")

print(order1)
print(order2)
