from django.urls import path 
from .views import BookListView
urlpatterns = [
    path('profile',BookListView.as_view(),name='profile')
]
