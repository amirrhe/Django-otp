from django.urls import path
from .views import *

urlpatterns = [
    path("send_sms/",request_send_verify_sms,name="send_sms"),
    path("verify/",verify_mobile_number,name="verify"),
]
