from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    established_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField(validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ], default=0.0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books"
    )
    genres = models.ManyToManyField("Genre", related_name="books", blank=True)

    def __str__(self):
        return self.title

    @property
    def genres_list(self):
        return ", ".join(self.genres.values_list("name", flat=True))


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
