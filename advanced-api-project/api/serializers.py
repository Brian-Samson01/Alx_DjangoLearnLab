from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

"""
BookSerializer:
- Serializes all fields of the Book model.
- Includes custom validation to ensure publication_year is not in the future.
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
- Serializes the Author model.
- Includes a nested BookSerializer to dynamically display related books.
- Uses the related_name 'books' defined in the Book model.
"""

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']