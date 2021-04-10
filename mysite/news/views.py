from django.shortcuts import render
from .models import News

# Create your views here.
def newspage(request,id=None):
    New = News.objects.all()
    
    
    params = {'News': New}
    
    return render(request,'news/newspage.html',params)

def News_detail(request, id=None):
    obj = News.objects.filter(news_id=id)
    print(obj)
    params={'objs':obj}
    return render(request, 'news/news_detail.html', params)

