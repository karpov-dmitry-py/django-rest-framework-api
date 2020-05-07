from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=500)
    year = models.IntegerField()
    category = models.CharField(max_length=300)
    director = models.CharField(max_length=150)

    def __str__(self):
        return f'({self.year}) {self.title}, {self.category}, directed dy: {self.director}'