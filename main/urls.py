from django.urls import  path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #main
    path('',Main.as_view()),
    #파일업로드 url링크 뒤에 '/' 를 빼야된다
    #main/upload
    path('upload',UploadFeed.as_view()),
]
# 이미지파일을 조회할 수 있어야하는데 이게 조회하는 코드임!

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)