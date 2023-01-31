from django.shortcuts import render


def homepage(request):
    return render(request, "enroll/homepage.html")


def company_list(request):
    return render(request, "enroll/company_list.html")


def car_list(request):
    return render(request, "enroll/car_list.html")
