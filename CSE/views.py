from django.shortcuts import render

from CSE.models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')


def students(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'student.html',context)

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')