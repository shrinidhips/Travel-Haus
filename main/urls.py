from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('index', views.index , name='index'),
    path('about',views.about , name='about'),
    path('tours',views.tours , name='tours'),
    path('contact',views.contact , name='contact'),
    path('test',views.test , name='test'),
    path('test1',views.test1 , name='test1'),
    path('test2',views.test2 , name='test2'),
    path('test3',views.test3 , name='test3'),
    path('test4',views.test4 , name='test4'),
    path('test5',views.test5 , name='test5'),
    path('test6',views.test6 , name='test6'),
    path('food',views.food , name='food')
]