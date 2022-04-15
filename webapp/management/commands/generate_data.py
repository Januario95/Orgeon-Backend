from django.core.management.base import (
    BaseCommand, CommandError
)
from webapp.models import Author, Book



class Command(BaseCommand):
    help = 'Generate data form the database'

    def handle(self, *args, **options):
        jk = Author.objects.create(name='J. K. Rowling')
        delia = Author.objects.create(name='Delia Owens')
        gabriel = Author.objects.create(name='Gabriel Marquez')
        scott = Author.objects.create(name='F. Scott Fitzgerald')
        leo = Author.objects.create(name='Leo Tolstoy')

        Book.objects.create(title='Harry Potter and the Cursed Child', author=jk)
        Book.objects.create(title='The Tales of Beedle the Bard', author=jk)
        Book.objects.create(title='Harry Potter: The Complete Series', author=jk)
        Book.objects.create(title='Fantastic Beasts and Where to Find', author=jk)
        Book.objects.create(title='The Casual Vacancy', author=jk)
        Book.objects.create(title='Quidditch Through The Ages', author=jk)

        Book.objects.create(title='Where the Crawdads Sing', author=delia)
        Book.objects.create(title='Secrets of the Savana', author=delia)
        Book.objects.create(title='Cry of the Kalahari', author=delia)
        Book.objects.create(title='The Eye of the Elephant', author=delia)

        Book.objects.create(title='One Hundred Years of Solitude', author=gabriel)
        Book.objects.create(title='Leaf Storm', author=gabriel)
        Book.objects.create(title='Love in the Time of Cholera', author=gabriel)
        Book.objects.create(title='Of Love and Other Demons', author=gabriel)

        Book.objects.create(title='The Great Gatsby', author=scott)
        Book.objects.create(title='Tender Is the Night', author=scott)
        Book.objects.create(title='This Side of Paradise', author=scott)

        Book.objects.create(title='War and Peace', author=leo)
        Book.objects.create(title='Anna Karenina', author=leo)

        self.stdout.write(self.style.SUCCESS(
            'Sucessfully created database'
        ))
