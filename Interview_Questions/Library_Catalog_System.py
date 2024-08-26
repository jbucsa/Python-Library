import os

class Item:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

class Book(Item):
    def __init__(self, title, author, year, genre, ISBN):
        super().__init__(title, author, year)
        self.genre = genre
        self.ISBN = ISBN

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nGenre: {self.genre}\nISBN: {self.ISBN}"

class DVD(Item):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nDuration: {self.duration} minutes"

    def display_details(self):
        base_info = super().display_info()
        return f"{base_info}\nDuration: {self.duration}"

def main():
    object_classes = {
        'Book': Book,
        'DVD': DVD
    }

    n = int(input())

    for _ in range(n):
        item_type, *attributes = input().split(',')
        attributes = [attr.strip() for attr in attributes]

        # Convert year and duration to int where applicable
        if item_type == 'Book':
            attributes[2] = int(attributes[2])  # year
        elif item_type == 'DVD':
            attributes[2] = int(attributes[2])  # year
            attributes[3] = int(attributes[3])  # duration

        item_class = object_classes[item_type]
        item = item_class(*attributes)

        print("--- Item Information ---")
        print(str(item))
        print(item.display_info())
        print("\nDetails:")

        if isinstance(item, DVD):
            print(item.display_details())
        else:
            print(item.display_info())
        print()

if __name__ == '__main__':
    main()
