from django.db import models

"""
Author model:
- Represents a book author.
- One author can write many books (one-to-many relationship).
"""

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book model:
- Represents a book written by an author.
- Each book is linked to exactly one author using a ForeignKey.
"""

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"