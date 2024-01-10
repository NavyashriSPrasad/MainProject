from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('logout/',views.LogoutPage,name='logout'),
    path('predict/',views.predictor,name='predictor'),
    #path('user/',views.user,name='user'),
    path('alcohol/', views.audit, name='audit'),  # Define your alcohol-related view and URL
    path('account/', views.account, name='account')
    
]
