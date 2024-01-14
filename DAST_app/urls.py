from django.urls import path
from . import views

urlpatterns = [
    path('',views.startPage,name='startPage'),
    path('login/',views.LoginPage,name='login'),
    #path('signup/',views.SignupPage,name='signup'),
    #path('signupAccount/',views.account_output,name='signupAccount'),
    path('logout/',views.LogoutPage,name='logout'),
    path('predictor/',views.predictor,name='Main'),
    #path('user/',views.user,name='user'),
    path('audit/', views.audit, name='auditTest'),  # Define your alcohol-related view and URL
    path('account/',views.account_output,name='account'),
    path('success_page/',views.success_page,name='success_page')
    #path('account', views.account_output, name='account')
    
    
]
