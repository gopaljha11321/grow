from email import message
from gc import collect
from django.shortcuts import render
from django.http import HttpResponse as hr;
from teach.models import Student
import pymongo
client=pymongo.MongoClient("mongodb+srv://gopaljha11321:jhaji9871436400@cluster0.cf4k1.mongodb.net/?retryWrites=true&w=majority")
db_name=client["grow"]
collection=db_name["teach_student"]
def index(request):
    return render(request,"teach_index.html")
def check(request):
    email=request.POST.get("email")
    password=request.POST.get("pass")
    print(email,password)
    data=collection.find({"email":email,"password":password})
   
    for i in data:
        try:
            print(i["fname"])
            return render(request,"dashboard.html",i)

        except:
            return render(request,"registration.html",i)
    message={
        "status":"Wrong username or password"
    }
    return render(request,"teach_index.html",message)
def update(request):
    data={
    "id":request.POST.get("email","default"),
    "fname":request.POST.get("fname","default"),
    "lname":request.POST.get("lname","default"),
    "email":request.POST.get("email","default"),
    "number":request.POST.get("number","default"),
    "address":request.POST.get("address","default"),
    "password":request.POST.get("password","default")
    }
    l1=[]
    l1.append(request.POST.get("python","default"));
    l1.append(request.POST.get("java","default"));
    l1.append(request.POST.get("cpp","default"));
    l1.append(request.POST.get("c","default"));
    l1.append(request.POST.get("web","default"));
    course=""
    for i in range(0,len(l1)):
        if(l1[i]!="default"):
            course+=l1[i];
            course+=",";
    course=course[0:len(course)-1];
    data["course"]=course
    # a=data["email"]
    # email=""
    # print(a)
    # for i in a:
    #     if(i!=" "):
    #         email+=i;
    get_mail=collection.find({"email":data["email"]})
    print("ram")
    for i in get_mail:
        print(i['fname'])
        collection.update({"email":data["email"]},data)
        print("data updated")
        return render(request,"teach_index.html")
    collection.insert(data)
    
    # print("insertion done!!")
    return render(request,"teach_index.html")
def reg(request):
    return render(request,'registration.html')

