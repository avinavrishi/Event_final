from django.urls import path
from . import views

urlpatterns = [

    path('',views.HomeView, name="Home_page"),
    path('event/',views.EventView, name="event_page"),
    path('event/detail/<int:id>',views.EventDetailView, name="event_Description_page"),
    path('about/',views.AboutView, name="about_page"),
    path('contact/',views.ContactView, name="contact_page"),
]
