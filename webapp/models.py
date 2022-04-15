from django.db import models



def format_books(books):
    str_books = ''
    for book in books:
        str_books += (f'"{book}"' + ',')

    return str_books.rstrip(',')


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_author_books(self):
        author_books = self.book_set.all()
        extract_title = [book.title for book in author_books]
        return f'{self.name}: {format_books(extract_title)}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


