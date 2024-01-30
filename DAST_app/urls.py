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
    path('success_page/',views.success_page,name='success_page'),
    path('pdf_page/',views.pdf_page,name='pdf_page'),
    path('pdf_page2/',views.pdf_page2,name='pdf_page2'),
    path('pdf_pageA/',views.pdf_pageA,name='pdf_pageA'),
    path('books/',views.books,name='books'),
     path('booksA/',views.booksA,name='booksA'),
     path('result/',views.result,name='result'),
      path('resultD/',views.resultD,name='resultD'),
      path('dashboard/',views.dashboard,name='dashboard'),
    path('read_book/<int:book_id>/', views.read_book, name='read_book')
    #path('account', views.account_output, name='account')
    
    
]
