import graphene
from graphene_django.types import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author):
        book = Book(title=title, author=author)
        book.save()
        return CreateBook(book=book)

class Query (graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root,info):
        return Book.objects.all()

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
