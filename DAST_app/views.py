from telnetlib import LOGOUT
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from joblib import load
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import LabelEncoder
from .models import Patient,Therapist,ArtConsultation
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Patient, TherapyAccess,Progress
from datetime import timedelta
from datetime import datetime
import plotly.express as px
import plotly.io as pio



model=load('./savedModels/new_svm.joblib')
model1=load('./savedModels/svm_audit.joblib')

# def HomePage(request):
#     return render(request,'home.html')

def startPage(request):
    return render(request,'startPage.html')

def pdf_page(request):
    return render(request,'pdf_page.html')
def pdf_page2(request):
    return render(request,'pdf_page2.html')
def pdf_pageA(request):
    return render(request,'pdf_pageA.html')

def yoga_therapy(request):
    return render(request,'yoga_therapy.html')

def books(request):
    return render(request,'books.html')

def booksA(request):
    return render(request,'booksA.html')

# def dashboard(request):
#     return render(request,'dashboard.html')

def dashboard(request):
    # Assuming you have logic to get the current patient object
    # Modify this according to your existing logic
    username = request.session.get('username', None)
    patient = Patient.objects.get(username=username)

    # Pass the patient to the template
    context = {
        'patient': patient,
    }

    # Render the dashboard template
    return render(request, 'dashboard.html', context)


def music_therapy(request):
    return render(request, 'music_therapy.html')

def music_therapy_ed(request):
    return render(request, 'music_therapy_ed.html')


def profile(request):
    username = request.session.get('username', None)
    patient = Patient.objects.get(username=username)
    consultations = ArtConsultation.objects.filter(patient_username=patient.username)

    context = {
        'patient': patient,
        'consultations': consultations
    }
    return render(request, 'profile.html', context)

def artTherapy(request):
    therapists= Therapist.objects.all()

    # Pass the therapists data to the template
    return render(request, 'artTherapy.html', {'therapists': therapists})



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('account')
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")

#     return render (request,'login.html')

# def LoginPage(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         password = request.POST.get('pass')

#         try:
#             # Check in Patient table
#             user = Patient.objects.get(username=uname)
#         except Patient.DoesNotExist:
#             try:
#                 # Check in Therapist table if not found in Patient table
#                 user = Therapist.objects.get(username=uname)
#             except Therapist.DoesNotExist:
#                 # User not found in both tables
#                 user = None

#         # if user is not None and password == user.password:
#         #     # Authentication successful
#         #     # You may want to store user details in the session or use Django's login system if needed
#         #     request.session['username'] = uname
#         #     return redirect('/success_page')
#         # else:
#         #     # Return an error message or handle invalid login
#         #     return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
#         if user is not None and password == user.password:
#             request.session['username'] = uname
#             # Check if the user has already chosen a concern and taken the test
#             if Patient.objects.filter(username=uname, Test_Result__isnull=False).exists():
#                 # Redirect to another page (e.g., a results page) if the user has already taken the test
#                 return redirect('dashboard')
#             else:
#                 # Redirect to the page where the user can choose their concern if they haven't done so yet
#                 return redirect('success_page')
#         else:
#             # Return an error message or handle invalid login
#             return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

        
   
#     return render(request, 'login.html')

def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('pass')

        try:
            # Check in Patient table
            user = Patient.objects.get(username=uname)
            is_patient = True
        except Patient.DoesNotExist:
            try:
                # Check in Therapist table if not found in Patient table
                user = Therapist.objects.get(username=uname)
                is_patient = False
            except Therapist.DoesNotExist:
                # User not found in both tables
                user = None
                is_patient = None

        if user is not None and password == user.password:
            request.session['username'] = uname
            if is_patient:
                # Check if the patient has already taken the test
                if user.Test_Result:
                    return redirect('dashboard')  # Redirect to dashboard if the patient has taken the test
                else:
                    # Check patient's concern and redirect accordingly
                    if user.concern == 'alcohol':
                        return redirect('success_page')  # Redirect to success_page if the patient's concern is alcohol
                    else:
                        return redirect('success_page2')  # Redirect to success_page2 for other concerns
            else:
                return redirect('therapist_consultation')  # Redirect therapists to their consultations page
        else:
            # Return an error message or handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
        
    return render(request, 'login.html')





def success_page(request):
    
    # if request.method=='POST':
    #   choice = request.POST.get('choice')
    #   username = request.session.get('username', None)
    #   user_details = Patient.objects.get(username=username)
    #   user_details.Test_Result = choice
    #   user_details.save()
    return render(request,'success_page.html')

def success_page2(request):
    
    return render(request,'success_page2.html')

def LogoutPage(request):
    LOGOUT(request)
    return redirect('login')

@login_required(login_url='login')
def user(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == 'a':  # Redirect to alcohol page
            return redirect('audit')   
        elif choice == 'd':  # drug page
            return redirect('predictor')  

    return render(request, 'user.html')

#@login_required(login_url='login')
# def predictor(request):
#     result_to_display = None
    
#     if request.method=='POST':
#         a1=request.POST['q1']
#         a2=request.POST['q2']
#         a3=request.POST['q3']
#         a4=request.POST['q4']
#         a5=request.POST['q5']
#         a6=request.POST['q6']
#         a7=request.POST['q7']
#         a8=request.POST['q8']
#         a9=request.POST['q9']
#         a10=request.POST['q10']
        
#         ypred=model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]])
        
#         if ypred[0]=='low level':
#             ypred='Low Level'
#         elif ypred[0]=='Moderate level':
#             ypred='Moderate Level'
#         elif ypred[0]=='Substantial level':
#             ypred='Substantial Level'
#         else:
#             ypred='Severe Level'
#         username = request.session.get('username', None)
#         user_details = Patient.objects.get(username=username)
#         user_details.Test_Result = ypred
#         user_details.save()
    
#         # result_to_display = ypred
#         return redirect('resultD')
#         # if ypred in ['Low Level', 'Moderate Level']:
#         #     # Redirect to 'books' page if the condition is met
#         #     return redirect('books')

#     return render(request, 'main.html')
    # return render(request, 'main.html', {'result': result_to_display})

def resultD(request):
    # Retrieve the result from the database
    username = request.session.get('username', None)
    user_details = Patient.objects.get(username=username)
    result = user_details.Test_Result
    
    return render(request, 'resultD.html', {'result': result})




# @login_required(login_url='login')
# def audit(request):
#     result_to_display = None
#     if request.method=='POST':
#         a1=request.POST['q1']
#         a2=request.POST['q2']
#         a3=request.POST['q3']
#         a4=request.POST['q4']
#         a5=request.POST['q5']
#         a6=request.POST['q6']
#         a7=request.POST['q7']
#         a8=request.POST['q8']
#         a9=request.POST['q9']
#         a10=request.POST['q10']
#         ypred=model1.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]])
#         if ypred[0]=='Alcohol Dependence':
#             ypred='Alcohol Dependence'
#         if ypred[0]=='Hazardous':
#             ypred='Hazardous'
#         if ypred[0]=='Low Risk':
#             ypred='Low Risk'
        
#         username = request.session.get('username', None)
#         user_details = Patient.objects.get(username=username)
#         user_details.Test_Result = ypred
#         user_details.save()
    
#         result_to_display = ypred
#         return redirect('result')
#         # if ypred == 'Low Risk':
#         #     # Redirect to 'booksA' page if the condition is met
#         #     return redirect('booksA')
        
#         #return render(request,'auditTest.html',{'result':ypred})
        
#     # return render(request,'auditTest.html',{'result':result_to_display})
#     return render(request,'auditTest.html')

def result(request):
    # Retrieve the result from the database
    username = request.session.get('username', None)
    user_details = Patient.objects.get(username=username)
    result = user_details.Test_Result
    
    return render(request, 'result.html', {'result': result})

# def account_output(request):
#     if request.method=='POST':
        
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
#         if pass1!=pass2:
#                 return HttpResponse("Your password and confrom password are not Same!!")
#         else:
#             en=details(fname=request.POST.get('fname'),lname=request.POST.get('lname'),username=request.POST.get('name'),
#                 age=request.POST.get('age'),gender=request.POST.get('gender'),dob=request.POST.get('dob'),
#                     address=request.POST.get('address'),city=request.POST.get('city'),state=request.POST.get('state'),phone=request.POST.get('phone'),
#                     employment=request.POST.get('employment'),education=request.POST.get('education'),concern=request.POST.get('choice'),password=request.POST.get('password1'))
#             en.save()
 
#     choice = request.POST.get('choice')
#     if choice == 'alcohol':# Redirect to alcohol page
#         return redirect('/audit')   
#     elif choice == 'drug':  # drug page
#         return redirect('/predictor') 
    
#     return render(request,'account.html')

def paccount_output(request):
    if request.method == 'POST':
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not the same!!")
            else:
                username = request.POST.get('uname')
                if Patient.objects.filter(username=username).exists():
                    return render(request, 'Paccount.html', {'error_message': 'Username already exists.'})
                
                patient = Patient(
                     fname=request.POST.get('fname'),
                    lname=request.POST.get('lname'),
                    username=username,
                    age=int(request.POST.get('age')),
                    gender=request.POST.get('gender'),
                    dob=request.POST.get('dob'),
                    address=request.POST.get('address'),
                    city=request.POST.get('city'),
                    state=request.POST.get('state'),
                    phone=request.POST.get('phone'),
                    employment=request.POST.get('employment'),
                    education=request.POST.get('education'),
                    concern=request.POST.get('choice'),
                    password=request.POST.get('password1')
                )
                patient.save()
                #messages.success(request, 'Patient account created successfully!')
                return redirect('login')
              

    return render(request, 'Paccount.html')

def taccount_output(request):
    if request.method == 'POST':
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not the same!!")
            else:
                username = request.POST.get('uname')
                if Therapist.objects.filter(username=username).exists():
                    return render(request, 'Taccount.html', {'error_message': 'Username already exists.'})
              
                therapist = Therapist(
                    fname=request.POST.get('fname'),
                    lname=request.POST.get('lname'),
                    username=username,
                    age=request.POST.get('age'),
                    gender=request.POST.get('gender'),
                    dob=request.POST.get('dob'),
                    address=request.POST.get('address'),
                    city=request.POST.get('city'),
                    state=request.POST.get('state'),
                    phone=request.POST.get('phone'),
                    qualification=request.POST.get('qual'),
                    experience=request.POST.get('exp'),
                    password=request.POST.get('password1')
                )
                therapist.save()
                #messages.success(request, 'Therapist account created successfully!')
                return redirect('login')

    return render(request, 'Taccount.html')
    
def read_book(request,id):
    book = PDFbooks.objects.get(id=id)
    return render(request, 'pdf_page.html', {'book': book})
    
# def audit(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         form_data = {
#             'q1': request.POST['q1'],
#             'q2': request.POST['q2'],
#             'q3': request.POST['q3'],
#             'q4': request.POST['q4'],
#             'q5': request.POST['q5'],
#             'q6': request.POST['q6'],
#             'q7': request.POST['q7'],
#             'q8': request.POST['q8'],
#             'q9': request.POST['q9'],
#             'q10': request.POST['q10']
#         }

#         # Encode categorical variables
#         encoded_form_data = {}
#         for feature, value in form_data.items():
#             if feature in label_encoders:
#                 label_encoder = label_encoders[feature]
#                 encoded_form_data[feature] = label_encoder.transform([value])[0]
#             else:
#                 encoded_form_data[feature] = value
        
#         # Prepare data for prediction
#         data_for_prediction = [[encoded_form_data[feature] for feature in form_data.keys()]]
        
#         # Make predictions using the model
#         y_pred = model.predict(data_for_prediction)
        
#         # Decode predictions
#         if y_pred == 0:
#             prediction = 'Alcohol Dependent'
#         elif y_pred == 1:
#             prediction = 'Hazardous'
#         else:
#             prediction = 'Low Level'

#         return render(request, 'auditTest.html', {'result': prediction})

#     return render(request, 'auditTest.html')


def artConsultation(request):
    if request.method == 'POST':
        therapist_username = request.POST.get('therapist_username')
        therapist = Therapist.objects.get(username=therapist_username)
        artwork = request.FILES['artwork']
        comments = request.POST['comments']

        # Retrieve the username from the session
        username = request.session.get('username', None)
        if username is None:
            # Handle the case when the username is not found in the session
            return render(request, 'username_not_found.html')

        # Attempt to retrieve the Patient instance
        try:
            patient = Patient.objects.get(username=username)
        except Patient.DoesNotExist:
            # Handle the case when the Patient instance is not found
            return render(request, 'error.html')

        # Create and save the ArtConsultation object with the patient assigned
        consultation = ArtConsultation.objects.create(patient_username=patient.username, therapist_username=therapist.username, artwork=artwork, comments=comments)
        consultation.save()

        return redirect('artConsultation')

    # Retrieve the username from the session
    username = request.session.get('username', None)
    if username is None:
        # Handle the case when the username is not found in the session
        return render(request, 'username_not_found.html')

    # Attempt to retrieve the Patient instance
    try:
        patient = Patient.objects.get(username=username)
    except Patient.DoesNotExist:
        # Handle the case when the Patient instance is not found
        return render(request, 'error.html')

    # Filter consultations based on the patient
    consultations = ArtConsultation.objects.filter(patient_username=patient.username)
    therapists = Therapist.objects.all()

    return render(request, 'artConsultation.html', {'therapists': therapists, 'consultations': consultations})


def therapist_consultation(request):
    therapist_username = request.session.get('username')
    
    if not therapist_username:
        # Handle the case when the therapist is not logged in
        return render(request, 'error.html')

    # Query consultations for the therapist
    consultations = ArtConsultation.objects.filter(therapist_username=therapist_username)
    
    return render(request, 'therapist_consultation.html', {'consultations': consultations})


def save_reply(request):
    if request.method == 'POST':
        # Get the consultation ID and the reply from the POST data
        consultation_id = request.POST.get('consultation_id')
        reply = request.POST.get('reply')

        # Retrieve the consultation object based on the ID
        try:
            consultation = ArtConsultation.objects.get(id=consultation_id)
        except ArtConsultation.DoesNotExist:
            messages.error(request, "Consultation not found.")
            return redirect('therapist_consultation')  # Redirect back to the therapist consultation page

        # Update the therapist_reply field with the new reply
        consultation.therapist_reply = reply
        consultation.save()

        messages.success(request, "Reply saved successfully.")
        return redirect('therapist_consultation')  # Redirect back to the therapist consultation page
    else:
        messages.error(request, "Invalid request method.")
        return redirect('therapist_consultation')  # Redirect back to the therapist consultation page

@csrf_exempt
def chat_socket(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        sender = request.POST.get('sender')
        message = request.POST.get('message')
        # Here, you should implement your logic to handle messages
        # For simplicity, we'll just echo the message back for now
        response_data = {
            'sender': sender,
            'message': message
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def patient_chat(request):
    return render(request, 'patient_chat.html')

def therapist_chat(request):
    return render(request, 'therapist_chat.html')

def error(request):
    # Render the error page template
    return render(request, 'error.html')

def affirmation(request):
    return render(request, 'affirmation.html')
    
def access_therapy(request, therapy_name):
    # Ensure the request method is POST
    if request.method != 'POST':
        print('Invalid request method')  # Add logging
        return redirect('error')

    # Retrieve the patient's username from the session
    patient_username = request.session.get('username')

    if not patient_username:
        print('No patient username found in session')  # Add logging
        return redirect('login')

    try:
        # Fetch the patient instance from the database
        patient = Patient.objects.get(username=patient_username)

        # Create a new TherapyAccess instance
        therapy_access = TherapyAccess(
            patient=patient,
            therapy_name=therapy_name,
            access_time=timezone.now()  # Record the current time
        )

        # Save the therapy access history to the database
        therapy_access.save()

        # Define a dictionary mapping therapy names to redirect URLs
        therapy_redirects = {
            'Knowledge Sessions': '/books/',
            'Mindfulness-Based Relapse Prevention (MBRP)': '/mbrp/',
            'Yoga Therapy': '/yoga_therapy/',
            'Affirmation Therapy': '/at/',
            'Art Therapy': '/artTherapy/',
            'Music Therapy': '/music_therapy/',
        }

        # Get the redirect URL
        redirect_url = therapy_redirects.get(therapy_name, '/errorp/')
        print('Redirect URL:', redirect_url)  # Add logging

        # Return the redirect URL as JSON
        return JsonResponse({'redirect_url': redirect_url})

    except Patient.DoesNotExist:
        print('Patient does not exist')  # Add logging
        return redirect('login')
    except Exception as e:
        print('Exception occurred:', e)  # Add logging
        return redirect('error')
    
    

# def progress_tracker(request):
#     # Retrieve the username from the session
#     username = request.session.get('username')
    
#     # Handle case when username is not in the session
#     if not username:
#         return render(request, 'error.html', {'message': 'Username not found in session.'})

#     # Get the patient object by username
#     patient = get_object_or_404(Patient, username=username)

#     # Get progress data for the patient
#     progress_data = Progress.objects.filter(patient=patient).order_by('-timestamp')
    
#     # Get the current progress (most recent)
#     current_progress = progress_data.first()

#     # Get the previous progress if available
#     previous_progress = progress_data[1] if len(progress_data) > 1 else None

#     # Determine the comparison between current and previous progress
#     result_comparison = None
#     if previous_progress:
#         if current_progress.result == previous_progress.result:
#             result_comparison = 'same'
#         elif current_progress.result > previous_progress.result:
#             result_comparison = 'improved'
#         else:
#             result_comparison = 'worse'
    
#     # If no progress data is available, encourage the patient to take the test again
#     if not current_progress:
#         return render(request, 'progress_tracker.html', {
#             'patient': patient,
#             'current_progress': None,
#             'previous_progress': None,
#             'result_comparison': None,
#             'no_progress_data': True,  # Indicate no progress data
#         })

#     # Render the progress tracker template with the patient's data and progress data
#     return render(request, 'progress_tracker.html', {
#         'patient': patient,
#         'current_progress': current_progress,
#         'previous_progress': previous_progress,
#         'result_comparison': result_comparison,
#         'no_progress_data': False,  # Indicate progress data is available
#     })

def progress_tracker(request):
    # Retrieve the username from the session
    username = request.session.get('username')
    
    # Handle case when username is not in the session
    if not username:
        return render(request, 'error.html', {'message': 'Username not found in session.'})

    # Get the patient object by username
    patient = get_object_or_404(Patient, username=username)
    
    # Get progress data for the patient
    progress_data = Progress.objects.filter(patient=patient).order_by('-timestamp')
    
    # Check if progress data is available
    current_progress = progress_data.first()
    previous_progress = progress_data[1] if len(progress_data) > 1 else None
    
    # Calculate the comparison between current and previous progress
    if previous_progress:
        if current_progress.result == previous_progress.result:
            result_comparison = 'same'
        elif current_progress.result > previous_progress.result:
            result_comparison = 'improved'
        else:
            result_comparison = 'worse'
    else:
        result_comparison = None
    
    # Get therapy access history for the patient
    therapy_access_history = TherapyAccess.objects.filter(patient=patient).order_by('-access_time')
    
    # Determine if there is no progress data available
    no_progress_data = not bool(progress_data)
    
    # Render the progress tracker template with the patient's data, progress data, and therapy access history
    return render(request, 'progress_tracker.html', {
        'patient': patient,
        'current_progress': current_progress,
        'previous_progress': previous_progress,
        'result_comparison': result_comparison,
        'no_progress_data': no_progress_data,
        'therapy_access_history': therapy_access_history,
    })
    
def predictor(request):
    result_to_display = None
    
    if request.method == 'POST':
        # Extract answers from the request
        a1 = request.POST['q1']
        a2 = request.POST['q2']
        a3 = request.POST['q3']
        a4 = request.POST['q4']
        a5 = request.POST['q5']
        a6 = request.POST['q6']
        a7 = request.POST['q7']
        a8 = request.POST['q8']
        a9 = request.POST['q9']
        a10 = request.POST['q10']
        
        # Get prediction
        ypred = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]])
        
        # Convert prediction to human-readable format
        if ypred[0] == 'low level':
            result = 'Low Level'
        elif ypred[0] == 'Moderate level':
            result = 'Moderate Level'
        elif ypred[0] == 'Substantial level':
            result = 'Substantial Level'
        else:
            result = 'Severe Level'
        
        # Get the username from the session
        username = request.session.get('username')
        
        # Get the patient object using the username
        patient = Patient.objects.get(username=username)
        
        # Check if this is the first test taken by the patient
        if patient.Test_Result is None:
            # Store the test result in the Patient model
            patient.Test_Result = result
            patient.save()
        else:
            # Store the test result in the Progress table for subsequent tests
            Progress.objects.create(patient=patient, result=result)
        
        # Redirect to the 'resultD' page
        return redirect('resultD')
    
    return render(request, 'main.html')


def audit(request):
    result_to_display = None
    
    if request.method == 'POST':
        # Extract answers from the request
        a1 = request.POST['q1']
        a2 = request.POST['q2']
        a3 = request.POST['q3']
        a4 = request.POST['q4']
        a5 = request.POST['q5']
        a6 = request.POST['q6']
        a7 = request.POST['q7']
        a8 = request.POST['q8']
        a9 = request.POST['q9']
        a10 = request.POST['q10']
        
        # Get prediction
        ypred = model1.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]])
        
        # Convert prediction to human-readable format
        if ypred[0] == 'Alcohol Dependence':
            result = 'Alcohol Dependence'
        elif ypred[0] == 'Hazardous':
            result = 'Hazardous'
        elif ypred[0] == 'Low Risk':
            result = 'Low Risk'
        
        # Get the username from the session
        username = request.session.get('username')
        
        # Get the patient object using the username
        patient = Patient.objects.get(username=username)
        
        # Check if this is the first test taken by the patient
        if patient.Test_Result is None:
            # Store the test result in the Patient model
            patient.Test_Result = result
            patient.save()
        else:
            # Store the test result in the Progress table for subsequent tests
            Progress.objects.create(patient=patient, result=result)
        
        # Redirect to the 'result' page
        return redirect('result')
    
    return render(request, 'auditTest.html')


# def dashboard(request):
#     username = request.session.get('username')
        
#         # Get the patient object using the username
  
#     try:
#           patient = Patient.objects.get(username=username)
#     except Patient.DoesNotExist:
#         return HttpResponse("Patient not found")

#     # Determine the addiction level of the patient
#     addiction_level = patient.Test_Result

#     # Define therapy options based on addiction levels
#     therapy_mapping = {
#         'Low Risk': ['Knowledge Sessions','Affirmation Therapy' , 'Music Therapy'],
#         'Hazardous': [ 'Yoga Therapy', 'Affirmation Therapy','CBT','Knowledge Sessions'],
#         'Alcohol Dependence': ['Music Therapy', 'Art Therapy', 'Yoga Therapy','Cognitive Behavioral Therapy (CBT)'],
#         'Low Level': ['Knowledge Sessions', 'Yoga Therapy', 'Affirmation Therapy'],
#         'Moderate Level': ['Knowledge Sessions', 'Music Therapy','Affirmation Therapy','Music Therapy','Affirmation Therapy'],
#         'Substantial Level': ['Art Therapy', 'Music Therapy','Affirmation Therapy' ,'Affirmation Therapy'],
#         'Severe Level': ['Yoga Therapy', 'CBT','Knowledge Sessions', 'Music Therapy', 'Affirmation Therapy']
#     }

#     # Get the therapies based on the addiction level
#     therapies = therapy_mapping.get(addiction_level, [])

#     # Pass the patient's data and therapies to the template
#     context = {
#         'patient': patient,
#         'therapies': therapies
#     }
    
#     return render(request, 'dashboard.html', context)

