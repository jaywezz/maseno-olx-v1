# Create your views here.
from django .urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'authentication'
urlpatterns = [
    path('register/', views.SignUp.as_view(), name='register'),
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    #path('sign_up/', views.sign_up, name='sign_up'),

    path('logout/', views.logout_view, name='logout'),

    #path('members/', views.member_details, name='sign_in'),
    #path('login/', TemplateView.as_view(template_name="authentication/user_reg.html")),
    #path('home/', views.welcome_page, name='welcome_page'),

   ]