from django.shortcuts import render
from .models import *
from rest_framework.response import Response
# Create your views here.
import random
import requests
from rest_framework.decorators import api_view
from django.http import HttpResponse
import redis 
r = redis.Redis()
def send_sms(text,number):
    """
        your logic for sending sms
    """
    pass


@api_view(http_method_names=['GET', 'POST'])
def request_send_verify_sms(request):
    phone_number = request.data['phone_number']
    if phone_number:
        if CustomUser.objects.filter(phone_number=phone_number).count()>=0:
            verification_code = random.randint(10000,99999)
            response = send_sms(text=verification_code,number=phone_number)
            r.setex("verification_code",180000,verification_code)
            return Response({"message": "ok"})
        else:
            return HttpResponse("this phone_number is not valid")
    else:
        return HttpResponse("please enter phone_number in request")
    
    
@api_view(http_method_names=['GET', 'POST'])
def verify_mobile_number(request):
    verification_code = request.data['verification_code']
    redis_verification_code=r.get("verification_code").decode("utf-8")
    if verification_code ==  redis_verification_code:
        return HttpResponse(f"verified true verification you send  {verification_code} and redis verifiction code is  {redis_verification_code}")
    else:
        return HttpResponse(f"verified false verification you send {verification_code} and redis verifiction code is {redis_verification_code}")