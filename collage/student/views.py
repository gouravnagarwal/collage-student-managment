from random import randint
from django.http import JsonResponse
from django.shortcuts import render

from student.models import Student
from django.core.mail import send_mail

# Create your views here.


def get_rollno(request):
    send_mail('important information',
              'this mail contain important information for you',
              'gouravnagarwal78@gmail.com',
              ['amaankhanak0003@gmail.com'])
    # n_otp=otp(5)
    # roll=request.GET.get('rno')
    # name=request.GET.get('nm')
    # d={"rollno":roll,"name":name}
    return JsonResponse("hyy my name is helloworld!",safe=False)

# get percentage according to rollno:-
def get_result(request):
    rno=request.GET.get('rollno')
    data=Student.objects.filter(rollno=rno)
    if len(data)==0:
        return JsonResponse("rollno not present",safe=False)
    percent=data[0].percentage
    if percent>60:
        division='first division'
    else:
        division='second division'
    
    result={"percentage":percent,"division":division}
    return JsonResponse(result,safe=False)
        
    

# this funcation is used to login for students:-
def login(request):
     print(request)
     print(request.POST)
     print(request.POST.get('username'))
     return JsonResponse("login sccessfull",safe=False)


# this funcation is used for profile create when we hit create API then data will 
# be store in database
def create(request):
    if request.method=="POST":
        rno=request.POST.get('rollno')
        nm=request.POST.get('name')
        ads=request.POST.get('address')
        percent=request.POST.get('percentage')
        student_ref=Student(rollno=rno,name=nm,address=ads,percentage=percent)
        student_ref.save()
        return JsonResponse("profile has been created successfully",safe=False)
    else:
        return JsonResponse("invalid method",safe=False)


# this funcation is used for delete data from database:-

def delete(request):
    rno=request.GET.get('rollno')
    data=Student.objects.filter(rollno=rno)
    data.delete()
    return JsonResponse("Entry delete successfully",safe=False)


# this funcation is used for update entry
def update(request):
    user_id=request.GET.get('id')
    user_address=request.GET.get("address")
    updated_id=Student.objects.get(id=user_id)
    updated_id.address=user_address
    updated_id.save()
    return JsonResponse("updated successfully",safe=False)

# this funcation is used to generate otp:-

def otp(digit):
    otp=[]
    for i in range(digit):
        num=randint(0,9)
        otp.append(str(num))
    return ''.join(otp)