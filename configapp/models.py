from django.db import models

class Student(models.Model):
    full_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=13)
    email=models.CharField(max_length=50)
    kurs=models.CharField(max_length=50)
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural="Students"
        ordering = ['-created_ed']



class Kurs(models.Model):
    title=models.CharField(max_length=50)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description=models.TextField(blank=True)
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural="Kurslar"
        ordering = ['-created_ed']