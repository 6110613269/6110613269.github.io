from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Student, Quota


# Create your views here.
# def index(request):
#     return render(request, "students/index.html", {
#         "students": Student.objects.all()
#     })

def student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student Not Found")
    return render(request, "students/student.html",{
            "student": student,
            "enrolls": student.quotas.all(),
            "non_enrolls": Quota.objects.exclude(quotas=student).all(),

            })

def back(request,student_id):
    return render(request, "students/index.html",{
            "students_id" : student_id,
            "students": Student.objects.get(pk=student_id)
        
    })

def book(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(pk=student_id)
        enroll = Quota.objects.get(pk=request.POST["enroll"])
        sits = enroll.quotas.all().count()
            
        if enroll.limit > sits and enroll.status == 'open':
            enroll.quotas.add(student)

            return HttpResponseRedirect(reverse("student", args=(student_id,)))
        else:
            return render(request, "students/error.html", {
        "students": Student.objects.all(),
        "student_id" : student_id
    })


def drop(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(pk=student_id)
        enroll = Quota.objects.get(pk=request.POST["enroll"])
        enroll.quotas.remove(student)
    return HttpResponseRedirect(reverse("student", args=(student_id,)))

