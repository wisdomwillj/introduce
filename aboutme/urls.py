from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # about_me 페이지가 홈 페이지 임
    #path('',views.index)
]