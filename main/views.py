
from django.shortcuts import render
from rest_framework.views import APIView
#초기의 장고 response
from rest_framework.response import Response
# Create your views here.
from .models import Feed
from uuid import uuid4
import os 
from config.settings.settings import MEDIA_ROOT


#GET으로보내면 
class Main(APIView):
    def get(self,request):
        #역순으로 꺼내오기
        feed_list=Feed.objects.all().order_by('-id')         #select * from contend_filed
        #딕셔너리형태임 dict는 context는 페이지에 전달하고자 하는 데이터를 넘겨줌 key=value형태로 넘기는거임
        return render(request,'main/main.html',context=dict(feeds=feed_list))

# 서버에 올리고 서버에서 받아주는 것을 만듬 
class UploadFeed(APIView):
    #
    def post(self,request):
        #클라이언트에서 -> 여기로옴 
        #일단  FILES를 넣어줘야 파일이 불어와짐
        file=request.FILES['file']
        #파일의 이름을 정하자 한글,파일,특수문자나 이름같은것을 파일 읽을때 고유 id 값을 줌
        uuid_name=uuid4().hex
        #미디어루트에다가 hex를 같이쓰겠다 
        # ~/media/uuidrandomqewqeq 
        save_path=os.path.join(MEDIA_ROOT,uuid_name)
        #파일을 읽어서 파일을 만들때 쓰는코드들
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
                
        image12 = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')      
        # print(file)
        # print(image)
        
        #새로만들때 
        Feed.objects.create(image=image12,content=content,user_id=user_id,profile_image=profile_image,like_count=0)
        
        return Response(status=200)