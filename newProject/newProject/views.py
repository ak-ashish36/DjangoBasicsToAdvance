from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html", data)


def aboutUs(request):
    # return HttpResponse("<h1>This is about us Page<h1/>")
    data = {"title": "About Page", "body": "This is about Page"}
    return render(request, "about.html", data)


def Course(request):
    data = {
        "title": "Home Page",
        "body": "Welcome to my new Project",
        "courses": ["Java", "Python", "C++"],
        "users": [
            {"name": "Ashish", "email": "ashish@gmail.com"},
            {"name": "Avimanyu", "email": "avimanyu@gmail.com"},
        ],
    }
    return render(request, "course.html", data)


def couserDetail(request, courseId):
    return HttpResponse("<h1>This is Course {id} Page <h1/>".format(id=courseId))
