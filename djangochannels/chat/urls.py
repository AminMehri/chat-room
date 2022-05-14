from django.urls import path, include
from chat.views import index, room
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name="index"),
    path('<str:room_name>/', room, name="room"),
    path('login', LoginView.as_view(template_name='chat/login.html'), name="login")
]
