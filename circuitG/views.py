from cgi import test
from email.headerregistry import Address
import numbers
from django.shortcuts import render
import random
from django.http import HttpResponse as hr;
from email.mime.text import MIMEText
import random
import ssl
import pymongo
import smtplib as sm
from twilio.rest import Client

client=pymongo.MongoClient("mongodb://localhost:27017")
db_name=client["grow"]
collection=db_name["intro_user"]

def mail_send(number,otp):
    phone_number="+14404673053"
    account_sid="AC50ddbbebfd6677c74426da6f20fe40fe"
    auth_token="7267d5c0e0a8eaefbd02b8c2bcb90663"
    client = Client(account_sid,auth_token)
        
    message_body="otp: ";
    number="+91"+str(number)
    print(type(number))
    #message = client.messages.create(body=message_body, from_=phone_number,to=number)
    print("Message sent!")
#    print(message.status)
    print("send otp")
    collection.insert({"id":"number","otp":otp,"number":number})
def index(request):
    # return hr("Product Page");
    return render(request,"circuitG_index.html")
def index_verify(request):
    otp=int(random.random()*1000000)
    user_data={
        "email":request.POST.get("email","deafult"),
        # "send":mail_send()
    }
    mail_send(user_data["email"],otp)
    return render(request,"circuitG_index_verify.html",user_data)
def login(request):
    otp_num=request.POST.get("otp","default")
    email=request.POST.get("email","default")
    data=collection.find({"number":email})
    otp_db=0
    for i in data:
        otp_db=i["otp"]
    otp_num=int(otp_num)
    if(otp_num==otp_db):
        data_user={
            "email":email
        }
        return render(request,"verify.html",data_user)
    else:
        feedback={
            "message":"Wrong OTP!",
            "email":email
        }
        return render(request,"circuitG_index_verify.html",feedback)
def update(request):
    name=request.POST.get("user_name");
    password=request.POST.get("password");
    password2=request.POST.get("password2");
    phone_number=request.POST.get("Phone Number")
    address=request.POST.get("address")
    email=request.POST.get("email")

    print("succefully update the data")
