from django.urls import path
from . import views

urlpatterns = [
    path('',views.newspage, name="newspage"),
    path('detail/<int:id>',views.News_detail, name="newspage"),
    


]
