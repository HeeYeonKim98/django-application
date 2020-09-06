from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListInfo.as_view()),
    path('<int:pk>/', views.DetailInfo.as_view()),
]
