from django.shortcuts import render
from .models import Student,Kurs

def student(request):
    student = Student.objects.all()

    context = {
        "student": student,
        "title": "Student"
    }
    db = {
        "full_name": "Student1",
        "phone_number": "+998965236514",
        "email": "abc@gmail.com",

    }
    return render(request, 'Student/index.html', context=context)

def kurs(request):
    kurs=Kurs.objects.all()

    context={
        "kurs":kurs,
        "title":"Kurs"
    }
    db={
        "title":
        "description"
    }
    return render(request, 'Student/index.html', context=context)
