from django.shortcuts import render
from rest_framework.views import APIView
#유저 만들기
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

# Create your views here.

class Join(APIView):
    def get(self,request):
        return render(request,'user/join.html')
    def post(self,request):
        # 회원가입
        email=request.data.get('email',None)
        nickname=request.data.get('nickname',None)
        name=request.data.get('name',None)
        password=request.data.get('password',None)
        
        #password 는 암호화가 되서 들어감
        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image='default_profile.jpg',
                            )
        return Response(status=200)
        

class Login(APIView):
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        # 로그인 
        pass