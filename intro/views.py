from stringprep import in_table_d1
from django.shortcuts import render
from django.http import HttpResponse as hr
from intro.models import Contect as c1
from email.mime.text import MIMEText
import random
import ssl
import pymongo
s_mail="jhagopal11321@gmail.com"
r_mail="gopaljha1321@gmail.com"
msg="""From: %s
To: To Person %s
Subject: Sending mail by smtplib in python
hii everyone hello welcome to the world
"""%(s_mail,r_mail)
from django.conf import settings
import smtplib as sm
client=pymongo.MongoClient("mongodb://localhost:27017")
db_name=client["grow"]
collection=db_name["intro_contect"]
def index(request):
    return render(request,"index.html");
def contect(request):
    data={
    "name" :request.POST.get("name","default"),
    "email" : request.POST.get("email","default"),
    "message" :request.POST.get("message","default")
    }
    print(data["name"],data["email"],data["message"])
    rendom_num = random.random()
    id_num=data["email"]+str(rendom_num)
    collection.insert({"id":id_num,"name":data["name"],"email":data["email"],"message":data["message"]})
    try:
        msg = MIMEText('Hi '+data["name"]+" thanks for reaching out! \nI shall contect you soon, please drop your number in mail ")
        msg['Subject'] = 'Thanks for Contacting us..!'
        msg['From'] = 'gopaljha11321@outlook.com'
        msg['To'] = 'gopaljha11321@gmail.com' 
        SSL_context = ssl.create_default_context()
        server= sm.SMTP("smtp-mail.outlook.com",587)
        server.starttls(context=SSL_context)
        print("login successfully")
        server.login("gopaljha11321@outlook.com","Gopal@2000")
        r_mail=data["email"]
        server.sendmail(s_mail,r_mail,msg.as_string());
        print("Successfully sent email")
    except:
        print("error occure to send")

    return render(request,"Contect.html",data)
# Create your views here.
