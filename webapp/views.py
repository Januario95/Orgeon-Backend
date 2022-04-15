from django.shortcuts import render
from django.db.models import (
    Value as V, CharField, Count
)
from django.db.models.functions import (
    Concat, Cast
)

from .models import Author, Book


def get_book_name():
    books = Book.objects.annotate(
        book_author=Concat(V('"'), 'title', V('". '),
            'author__name', output_field=CharField()))
    for book in books:
        print(book.book_author)



def format_books(books):
    str_books = ''
    for book in books:
        str_books += (f'"{book}"' + ',')

    return str_books.rstrip(',')



def get_author_books():
    authors = Author.objects.all()
    for author in authors:
        author_books = author.book_set.values_list('title')
        extract_titles = [book[0] for book in author_books]
        print(f'{author.name}: {format_books(extract_titles)}')




def get_author_nr_of_books():
    author_books = Author.objects.annotate(
        author_name=Cast('name', output_field=CharField()),
        number_of_books=Count('book__title')
    )
    for a_b in author_books.order_by('-number_of_books'):
        print(f'{a_b.author_name}: {a_b.number_of_books}')



