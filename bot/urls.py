from bot import views
from django.urls import path

urlpatterns = [
    path("webhook", views.WebHook.as_view()),
]
