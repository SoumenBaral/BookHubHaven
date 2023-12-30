from django.urls import path,include
from .views import BookView


urlpatterns = [
 path('book/',BookView.as_view(),name='book'),
 path('category/<slug:category_slug>/',BookView.as_view(), name='category_wise_post'),
]