from django.urls import path
from .views import PersonAPI, PersonDetail


urlpatterns = [
    path('personApi/', PersonAPI.as_view()),
    path('person-retrive/<int:pk>/',PersonDetail.as_view()),
]