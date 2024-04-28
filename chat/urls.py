from django.urls import path
from .views import chat,blog



urlpatterns = [
    path('chat/',chat,name='chat'),
    path('blog/',blog,name='blog')
]