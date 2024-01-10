from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from joblib import load
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import LabelEncoder
from .models import userinfo


model=load('./savedModels/best_svm.joblib')
model1=load('./savedModels/rf_model.joblib')

def HomePage(request):
    return render(request,'home.html')

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

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('account')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

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

@login_required(login_url='login')
def predictor(request):
    if request.method=='POST':
        a1=request.POST['q1']
        a2=request.POST['q2']
        a3=request.POST['q3']
        a4=request.POST['q4']
        a5=request.POST['q5']
        a6=request.POST['q6']
        a7=request.POST['q7']
        a8=request.POST['q8']
        a9=request.POST['q9']
        a10=request.POST['q10']
        ypred=model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]])
        if ypred[0]=='low level':
            ypred='Low Level'
        elif ypred[0]=='Moderate level':
            ypred='Moderate Level'
        elif ypred[0]=='Substantial level':
            ypred='Substantial Level'
        else:
            ypred='Severe Level'
        
        return render(request,'main.html',{'result':ypred})
    return render(request,'main.html')

@login_required(login_url='login')
def audit(request):
    if request.method=='POST':
        a1=request.POST['q1']
        a2=request.POST['q2']
        a3=request.POST['q3']
        a4=request.POST['q4']
        a5=request.POST['q5']
        a6=request.POST['q6']
        a7=request.POST['q7']
        a8=request.POST['q8']
        a9=request.POST['q9']
        a10=request.POST['q10']
        ypred=model1.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]])
        if ypred==0:
            ypred='Alcohol Dependent'
        if ypred==1:
            ypred='Hazardous'
        if ypred==2:
            ypred='Low level'
        
        return render(request,'auditTest.html',{'result':ypred})
    return render(request,'auditTest.html')

# def account(request):
#     return render(request,'account.html')
def account_output(request):
    en=userinfo(uname=request.POST.get('name'),age=request.POST.get('age'),gender=request.POST.get('gender'),dob=request.POST.get('dob'),
                address=request.POST.get('address'),city=request.POST.get('city'),state=request.POST.get('state'),phone=request.POST.get('phone'),
                employment=request.POST.get('employment'),education=request.POST.get('education'),concern=request.POST.get('choice'))
    en.save()
    #str1="Data inserted to userinfo table" 
    choice = request.POST.get('choice')
    if choice == 'alcohol':  # Redirect to alcohol page
        return redirect('audit')   
    elif choice == 'drug':  # drug page
        return redirect('predictor') 
    
    str1="Data inserted to student table" 
    return render(request,'account.html',{'msg':str1})
    

    
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




