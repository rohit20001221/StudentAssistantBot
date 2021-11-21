from django.db import models

# Create your models here.


class Subject(models.Model):

    DIFFICULTY_CHOICES = [("easy", "easy"), ("medium", "medium"), ("hard", "hard")]

    name = models.CharField(max_length=200, unique=True)
    difficulity = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"


class Document(models.Model):
    url = models.URLField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="documents"
    )

    def __str__(self):
        return self.url

    class Meta:
        db_table = "document"
