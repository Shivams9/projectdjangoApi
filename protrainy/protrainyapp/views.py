import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from .models import protrainyModel


# from django.contrib.auth import authenticate, login
# Create your views here.


def test(request):
    name = "sachin"
    job = "flutter"
    return render(request, "sign.html", {"name": name, "job": job})


def create(request):
    try:
        user_type = 0
        name = 0
        user_name = 0
        user_branch = 0
        user_password = 0
        submit = 0
        if request.POST:
            name = request.POST["name"]
            user_type = request.POST["user_type"]
            user_name = request.POST["user_name"]
            user_branch = request.POST["user_branch"]
            user_password = request.POST["user_password"]

            opt = request.POST["option"]
            p = protrainyModel()
            p.user_type = user_type
            p.name = name
            p.user_name = user_name
            p.user_branch = user_branch
            p.user_password = user_password

            p.save()
            print("saved")

            if opt == "submit":
                submit = name
                # if user_type == "Admin":
                return redirect(login)
        return render(request, 'sign.html', {'message': "saved"})  # This IS POST
    except:
        error = {'status': 'failed'}
        return JsonResponse(error)


def jsonall(request):
    output = serializers.serialize("json", protrainyModel.objects.all())
    # return JsonResponse(output,safe=False)
    return HttpResponse(output, content_type="application/json")


def notification(request):
    n = len(protrainyModel.objects.all())
    data = {"count": n}
    data = json.dumps(data)
    response = HttpResponse(data, content_type='application/json')

    response["Access-Control-Allow-Origin"] = "*"
    response["Cross-Origin-Opener-Policy"] = "*"
    return response

    # return render(request, "sign.html",  #This is GET
    #      {"user_type":user_type,"name":name,"user_name": user_name, "user_branch": user_branch, "user_password": user_password, "submit": submit})


def read(request):
    protrainy = protrainyModel.objects.all()
    return render(request, "read.html", {'protrainys': protrainy})


def reads(request):
    protrainy = protrainyModel.objects.all()
    return render(request, "security.html", {'protrainys': protrainy})


def edit(request):
    id = request.GET["id"]
    protrainy = protrainyModel.objects.get(id=id)
    return render(request, 'edit.html', {'protrainys': protrainy})


def check(request):    #for redirect and write value pass and wrong
    id=request.GET['id']
    protrainy = protrainyModel.objects.filter(id=id)
    protrainy= protrainy[0]
    print(protrainy)
    protrainy.verify="pass"
    protrainy.save()
    return redirect(reads)

    return render(request, 'a.html')
def check2(request):
    id = request.GET['id']
    protrainy = protrainyModel.objects.filter(id=id)
    protrainy = protrainy[0]
    print(protrainy)
    protrainy.verify = "Wrong"
    protrainy.save()
    return redirect(reads)

    return render(request, 'b.html')


def verify(request):
    name = ""
    user_name = ""
    user_branch = ""

    if request.GET:
        name = request.GET["name"]
        user_password = request.GET["user_name"]
        user_branch = request.GET["user_branch"]
        records = protrainyModel.objects.filter(verify != 'absent')
        print(records)
        n = len(records)
        if n < 1:
            print("Invalid")
        else:
            print("ok")

    return render(request, 'home.html', {'name': name, 'user_name': user_name, 'user_branch': user_branch})


def login(request):
    user_name = ""
    user_password = ""

    if request.GET:
        user_name = request.GET["user_name"]
        user_password = request.GET["user_password"]
        records = protrainyModel.objects.filter(user_name=user_name, user_password=user_password)
        print(records)
        n = len(records)
        if n < 1:
            print("Invalid")
        else:
            print("ok")
            record = records[0]
            print(record)
            user_type = record.user_type
            print(user_type)
            if user_type == "Admin":
                return redirect(read)
            if user_type == "Security":
                return redirect(reads)
            # if user_type == "user":
            #     return redirect(read)
        opt = request.GET['option']

    return render(request, "login.html", {'user_name': user_name, 'user_password': user_password})


# def login(request):
#     if request.GET:
#         user_name = request.GET["user_name"]
#         user_password = request.GET["user_password"]
#         # user_password = request.GET["user_password"]
#     # user_name = 0
#     # user_password = 0
#     # x="anand"

#         protrainy = protrainyModel.objects.filter(user_name=user_name,user_password=user_password)
#         n=len(protrainy)
#         if n<=0:
#             print("No  record")
#         else:
#             print("Found")
#             currentrecord=protrainy[0]
#             print(currentrecord.user_type,user_password)
#         print(protrainy,n)
#     return render(request, "login.html", {'user_name': currentrecord.user_name,'user_password':currentrecord.user_password})


def delete(request):
    if request.GET:
        id = request.GET["id"]
        protrainy = protrainyModel.objects.filter(id=id)[0]

        protrainy.delete()

    return render(request, "delete.html", {"protrainys": protrainy})
