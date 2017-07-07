# graphqlserver

Process GraphQL requests in Django.

```python
from graphqlserver import Serializer, Query, Mutation
from .models import Book

class BookSerializer(Serializer):
    class Meta:
        model = Book
        required_fields = ('title',)

class BooksQuery(Query):
    queryset = Book.objects.all()

class CreateBookMutation(Mutation):
    serializer_class = BookSerializer
```
