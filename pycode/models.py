from django.db import models

# Create your models here.

class PostCode(models.Model):
    head = models.CharField(max_length=30) # 파이썬, 크롤링, 머신러닝, Django, Hadoop플랫폼 등 구분
    head_image = models.ImageField(upload_to='portfolio/images/', blank=True) # head에 관련된 사진 등록
    title = models.CharField(max_length=30) # 코드에 관한 제목
    ideenv = models.CharField(max_length=30) # 개발환경
    content = models.TextField() # 문자열의 제한이 없는 TextField()를 사용
    file_upload = models.FileField(upload_to='portfolio/files/', blank=True) # 코드 파일 등록
    created_at = models.DateTimeField(auto_now_add=True) # 월, 일,시,분, 초까지 기록해주는 필드
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/portfolio/{self.pk}'