from django.urls import path 
from .views import main ,main2, main3
urlpatterns=[
    path('',main),
    path('blogin',main2,name='blogin'),
    path('blogin1',main3,name='blogin1')
]

