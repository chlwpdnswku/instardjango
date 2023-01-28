from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로파일 사진
        유저 닉네임        -> 화면에 표기되는 이름 
        유저 이름         ->실제 사용자 이름 
        유저 이메일 주소    -> 회원가입 사용하는 아이디
        유저 비밀번호      -> 디폴트로 쓰기
    """
    profile_image   =models.TextField()
    nickname        =models.CharField(max_length=24,unique=True)
    name            =models.CharField(max_length=24)
    email           =models.EmailField(unique=True)
    
    #실제로 유저를 선택하면 유저의 이름을 쓸꺼냐 회원가입할때 필요한내용들인듯 table에 auth_user를 없애는 부분임이게
    USERNAME_FIELD='nickname'
    
    class Meta:
        db_table="User"