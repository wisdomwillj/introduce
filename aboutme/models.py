from django.db import models

# Create your models here.

class Post_aboutme(models.Model):
    myname = models.CharField(max_length=30, null=True, blank=True) # 본인이름
    myemail = models.CharField(max_length=30, null=True, blank=True)  # 이메일
    myaddress = models.CharField(max_length=30, null=True, blank=True)  # 주소
    highshool_name = models.CharField(max_length=30, null=True, blank=True)  # 고등학교 이름
    high_start = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) # 고등학교 입학년도
    high_end = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)  # 고등학교 졸업년도
    university_name = models.CharField(max_length=30, null=True, blank=True)  # 대학교 이름
    uni_start = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) # 대학교 입학년도
    uni_end = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)  # 대학교 졸업년도
    content = models.TextField(null=True) # 자기소개
    def __str__(self): # 포스트 제목과 번호를 보여주기
        return f'[{self.pk}]{self.myname}' # 장고의 모델은 기본적으로 primary key(pk)를 만듦
                                           # pk값으로 1,2,3,-- 등 자동으로 번호 생성