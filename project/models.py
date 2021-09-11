from django.db import models

# Create your models here.

class Post(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True) # 회사이름
    department = models.CharField(max_length=30, null=True, blank=True)  # 부서명
    position = models.CharField(max_length=30, null=True, blank=True)  # 직위
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) # project 참여 시작일
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) # project 참여 종료일
    content = models.TextField(null=True) # project 소개 및 활동내용

    def __str__(self): # 포스트 제목과 번호를 보여주기
        return f'[{self.pk}]{self.company_name}' # 장고의 모델은 기본적으로 primary key(pk)를 만듦
                                                 # pk값으로 1,2,3,-- 등 자동으로 번호 생성

    def get_absolute_url(self): # project의 상세페이지로 이동할 때 자동으로 pk값을 불러오는 url 생성규칙을 정의
        return f'/project/{self.pk}' # pk값을 자동으로 받아서 이동경로 형성