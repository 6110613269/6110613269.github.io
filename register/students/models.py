from django.db import models

# Create your models here.

class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    username = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.first} {self.last}"
        
class Quota(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    limit = models.PositiveIntegerField()
    status = models.CharField(max_length=64)
    quotas = models.ManyToManyField(Student, blank=True, related_name="quotas")

    def __str__(self):
        return f"{self.code}: {self.name}"
        
    def is_valid_limit(self):
        return self.limit >= self.quotas.all().count()

    def is_valid_open(self):
        return self.status == "open"

