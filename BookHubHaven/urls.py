from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Core.urls')),
    path('member/',include('Members.urls'))
]
