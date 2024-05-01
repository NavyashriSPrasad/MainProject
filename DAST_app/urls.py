from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.startPage,name='startPage'),
    path('login/',views.LoginPage,name='login'),
    #path('signup/',views.SignupPage,name='signup'),
    #path('signupAccount/',views.account_output,name='signupAccount'),
    path('logout/',views.LogoutPage,name='logout'),
    path('predictor/',views.predictor,name='Main'),
    #path('user/',views.user,name='user'),
    path('audit/', views.audit, name='auditTest'),  # Define your alcohol-related view and URL
    path('Paccount/',views.paccount_output,name='Paccount'),
    path('Taccount/',views.taccount_output,name='Taccount'),
    path('success_page/',views.success_page,name='success_page'),
    path('success_page2/',views.success_page2,name='success_page2'),
    path('pdf_page/',views.pdf_page,name='pdf_page'),
    path('pdf_page2/',views.pdf_page2,name='pdf_page2'),
    path('pdf_pageA/',views.pdf_pageA,name='pdf_pageA'),
    path('books/',views.books,name='books'),
    path('yoga_therapy/',views.yoga_therapy,name='yoga_therapy'),
    path('music_therapy/', views.music_therapy, name='music_therapy'),
     path('music_therapy_ed/', views.music_therapy_ed, name='music_therapy_ed'),
      path('music_therapy/music_therapy_ed.html', views.music_therapy_ed, name='music_therapy_ed'),
     path('booksA/',views.booksA,name='booksA'),
     path('result/',views.result,name='result'),
      path('resultD/',views.resultD,name='resultD'),
      path('dashboard/',views.dashboard,name='dashboard'),
    # path('artTherapy/',views.artTherapy,name='artTherapy'),
      path('artTherapy/',views.artTherapy,name='artTherapy'),
      path('therapist_consultation/',views.therapist_consultation,name='therapist_consultation'),
       path('save_reply/', views.save_reply, name='save_reply'),
      path('artConsultation/', views.artConsultation, name='artConsultation'),
      path('therapist_chat/',views.therapist_chat,name='therapist_chat'),
       path('patient_chat/',views.patient_chat,name='patient_chat'),
      path('profile/',views.profile,name='profile'),
       path('affirmation/',views.affirmation,name='affirmation'),
      path('error/', views.error, name='error'),
      path('access_therapy/<str:therapy_name>/', views.access_therapy, name='access_therapy'),
    path('progress_tracker/', views.progress_tracker, name='progress_tracker')
    #path('progress_tracker/<int:patient_id>/', views.progress_tracker, name='progress_tracker')
    
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)