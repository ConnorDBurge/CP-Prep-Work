from django.db import models


class Cohort(models.Model):
    cohort_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    end_date = models.CharField(max_length=200)

    def __str__(self):
        return f'Cohort {self.cohort_name}'


class Student(models.Model):
    cohort = models.ForeignKey(
        Cohort, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
