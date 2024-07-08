from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms

def home(request):
    return render(request, "index.html",)


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

def contactUs(request):
    return render(request, "contact.html")

def couserDetail(request, courseId):
    return HttpResponse("<h1>This is Course {id} Page <h1/>".format(id=courseId))

def useForm(request):
    fn=userForms()
    data={"form":fn}
    try:
        if(request.method=="GET"):
            n1=int(request.GET['num1'])
            n2=int(request.GET.get('num2'))
            print(n1+n2)
            data={"n1":n1,"n2":n2,"output":n1+n2,"form":fn}

        if(request.method=="POST"):
            n1=int(request.POST['num1'])
            n2=int(request.POST.get('num2'))
            print(n1+n2)
            data={"n1post":n1,"n2post":n2,"outputpost":n1+n2,"form":fn}
            # redirecting to course page
            url="/course/?output={}".format(data["outputpost"])
            return HttpResponseRedirect(url)
    except:
        pass

    return render(request, "form.html",data)