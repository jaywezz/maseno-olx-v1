
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item_view.urls')),
    path('', include('authentication.urls')),
   # path('', include('django.contrib.auth.urls')),

]
