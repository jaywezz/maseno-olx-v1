from django .urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
app_name = 'item_view'
urlpatterns = [
    path('', views.welcome_page, name= 'welcome_page'),
    path('categories/', views.categories, name='categories'),
    path('upload-product/', views.UploadView.as_view(), name='upload_product'),
    path('<name>/update-product/', views.UpdateView.as_view(), name='update_product'),
    path('item_list/', views.item_list, name='item_list'),
   path('item_detail/<name>', views.item_detail, name='item_detail'),
    path('category/<category_name>', views.categories, name='category'),
    path('profile', views.profile, name='profile'),
    path('header', views.header, name='header'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

