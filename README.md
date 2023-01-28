# 장고프로젝트 시작 

```
자동 정렬해주는 프로그램
Unibeautify - Universal Formatter
```
### html 20가지 꿀팀 사이트 https://parkjh7764.tistory.com/93

```
django-admin startproject config .
```

# gitignore 파일 만들기


# static과 template 파일 설정하기 

```
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
# config setting파일 
```

'DIRS': [BASE_DIR / 'templates'],

```

# 시간대와 한글 설치하기

```
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

```

# static 부트스트랩 적용시키기 


``` 프로젝트만들기
python manage.py startapp content

```


# REST 프레임워크 
```
pip install djangorestframework
```


# 구글 머터리얼 아이콘
```
https://developers.google.com/fonts/docs/material_icons
에 들어가면 있는데 

<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
이걸 적용시켜줌
```

# how to get google material icons?
```
https://stackoverflow.com/questions/50303454/how-to-use-the-new-material-design-icon-themes-outlined-rounded-two-tone-and
```

# flex 
```

https://studiomeal.com/archives/197
```

## ORM의장점 
- 쿼리를 안써도됨 코드를 SQL을 바꿔줌 쿼리셋
```
    일단 왜래키를 사용을 안함 이프로젝트에는
    피드 데이터
    ID값  / 프로필주소 /글쓴이름/ 이미지/ 글내용 

    +

    댓글 데이터 
    피드ID/ 댓글글쓴이/ 댓글내용/

    좋아요 데이터
    피드id /좋아요한사람/좋아요외부

```

## 자바스크립트 활용자료

``` 
stopPropagenation()은 이벤트가 상위 페이지로 가지않도록 전파되지 않는것이다 .

```
https://kutar37.tistory.com/entry/HTML5-Javasciprt-DragDrop-%EA%B5%AC%ED%98%84-%EC%98%88%EC%A0%9C


## 자바스크립트 이미지파일과 글 파일 올라가는 
### modal창에서 -> img를 올린 다음 -> 글쓰는 창으로 넘어가는것으로 작동을시키는데 -> 모달창을 2개로 하는식으로 해보기
```
  // 여기서 종요한것 ! e.target 이 있는데 target으로 하지말고 class 명으로해보기!
      $('.img_drop').css({
        "background-image": "url(" + window
          .URL
          .createObjectURL(files[0]) + ")",
        "outline": "none",
        "background-size": "100% 100%"
      });

```

## ajax 사용
```
데이터베이스는 파일이 실제로 안들어감 
파일은 -> 파일서버에 들어간다고함 
주소만 DB에넣어주는거임 ! 
```

## 검색어 키워드 
- ajax 파일업로드
- 미디어파일 업로드
- jquery ajax
- django file 업로드
- 템플릿에서 media 경로 사용하기
- 장고 유저모델 settings 
- django 패스워드 만들기 django make password

https://velog.io/@kong2520/Django-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8

### 현재 브라우저 + 파일,정보,사용자이름,프로필,글내용
    -> view.py의 ajax로 보냈음 uploadFeed() -> dB에 생성이되고 ->브라우저에 새로고침을해서 웹이 올려짐

### 장고는 기본템플릿이 USER 모델이 좋긴함 (사용자 모델을 꼭 먼저 정해야하는게 중요시함 !)
    1.하지만 우리가 원하는 필드가 없을지 모르니까 상속을받아서 CUSTOM USER MODEL을 만들 수 있음(기존 유저모델)
    - 장점 개편함 
    2.완전새로운 USERMODEL 만들기 가능 
    - 이거는 전부 새로 만들어줘야됨 
    AbstractBaseUser 이거만상속받으면됨 ㅇㅇ 
# 장고 커스템모델 링크
https://dev-yakuza.posstree.com/ko/django/custom-user-model/

# ajax를 통해서 실제회원가입을 만들고 api를 만들기

## 단향향 , 양방향 암호화
- 단방향 : 암호화된 것을 원래대로 못돌림 암호회시키면 끝임! 패스워드는 보통 단방향
- 양방향 : 암호화된 키를 복호화가 가능함 !  주민번호는 이걸 씀


### 장고 패스워드 암호화
https://cjh5414.github.io/create-django-user-instance-with-hashed-password/

### ajax rest api 호출  # instardjango
