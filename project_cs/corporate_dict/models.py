from django.db import models

class CorporateTerm(models.Model):
    word = models.CharField(max_length=100, unique=True)  # Term or jargon
    definition = models.TextField()  # Definition of the term

    def __str__(self):
        return self.word