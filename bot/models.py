from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "branch"


class Semister(models.Model):
    number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name="semisters"
    )

    def __str__(self):
        return self.branch.name + "/" + str(self.number)

    class Meta:
        db_table = "semister"


class Subject(models.Model):

    DIFFICULTY_CHOICES = [("easy", "easy"), ("medium", "medium"), ("hard", "hard")]

    name = models.CharField(max_length=200)
    cradits = models.IntegerField(validators=[MaxValueValidator(4)])
    difficulity = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    semister = models.ForeignKey(
        Semister, on_delete=models.CASCADE, related_name="subjects"
    )

    def __str__(self):
        return str(self.semister) + "/" + self.name

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


"""
    CREATE TABLE document (
        url VARCHAR(1000) NOT NULL,
        subject INTEGER NOT NULL,
        FOREIGN KEY subject REFERENCES subject(id)
    );
"""
