from curses.ascii import HT
import email
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

constactNumber = "+212 623011 384"
mail = "olaitanorganization@gmail.com"

def index(request):
    return render(request,"app1/index.html", {
        "contactNumber": constactNumber,
        "email": mail
    })

def about(request):
    return render(request,"app1/about.html", {
        "contactNumber": constactNumber,
        "email": mail
    })

def contact(request):
    return render(request,"app1/contact.html",{
        "contactNumber": constactNumber,
        "email": mail
    }) 



# def blog(request):
#     return render(request,"app1/blog.html", {
#         "contactnumber": constactNumber,
#         "email": mail
#     })

# def project(request):
#     return render(request,"app1/project.html", {
#         "contactnumber": constactNumber,
#         "email": mail
#     })

def team(request):
    return render(request,"app1/team.html", {
        "contactNumber": constactNumber,
        "email": mail
    })


def service(request):
    return render(request,"app1/service.html", {
        "contactNumber": constactNumber,
        "email": mail
    })