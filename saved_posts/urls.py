from django.urls import path
from saved_posts import views

urlpatterns = [
    path('savedposts/', views.SavedPostList.as_view()),
]