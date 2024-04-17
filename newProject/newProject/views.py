from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to this new Project")
    
def aboutUs(request):
    return HttpResponse("<h1>This is about us Page<h1/>")

def Course(request):
    return HttpResponse("<h1>This is Courses Page<h1/>")

def couserDetail(request,courseId):
    return HttpResponse("<h1>This is Course {id} Page <h1/>".format(id=courseId))