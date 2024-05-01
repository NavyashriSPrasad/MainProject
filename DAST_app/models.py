from django.db import models



# Create your models here.

# class userinfo(models.Model):
#     # Define fields for your table
#     id = models.AutoField(primary_key=True,default=1)
#     username = models.CharField(max_length=50 )
#     fname=models.CharField(max_length=100)
#     lname=models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=100)
#     dob = models.DateField()
#     address = models.CharField(max_length=500)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     employment = models.CharField(max_length=100)
#     education = models.CharField(max_length=100)
#     concern = models.CharField(max_length=100)
#     Test_Result=models.CharField(max_length=50)
#     class Meta:
#         db_table='userinfo'

# class details(models.Model):
#     account_type=models.CharField(max_length=100,default='patient')
#     fname=models.CharField(max_length=100)
#     lname=models.CharField(max_length=100)
#     username = models.CharField(max_length=50,primary_key=True)
#     password = models.CharField(max_length=100,default='default_password')
#     age = models.IntegerField()
#     gender = models.CharField(max_length=100)
#     dob = models.DateField()
#     address = models.CharField(max_length=500)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     employment = models.CharField(max_length=100)
#     education = models.CharField(max_length=100)
#     qualification= models.CharField(max_length=100, default='')
#     Experience=models.IntegerField(default=0)
#     concern = models.CharField(max_length=100)
#     Test_Result=models.CharField(max_length=50)
#     class Meta:
#         db_table='details'

class Patient(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    dob = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    employment = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Test_Result = models.CharField(max_length=50, null=True)
    class Meta:
        db_table='Patient'

class Therapist(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    dob = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    password = models.CharField(max_length=100)
    class Meta:
        db_table='Therapist'
    
# class PDFbooks(models.Model):
#     title=models.CharField(max_length=100)
#     pdf_content = models.BinaryField()   
#     class Meta:
#         db_table='PDFbooks'
        

class ArtConsultation(models.Model):
    patient_username = models.CharField(max_length=150)
    therapist_username = models.CharField(max_length=150)
    artwork = models.ImageField(upload_to='artwork/')
    comments = models.TextField()
    therapist_reply = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ArtConsultation'
        

class TherapyAccess(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapy_name = models.CharField(max_length=100)
    access_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'TherapyAccess'


from django.utils import timezone

class Progress(models.Model):
    # ForeignKey to link the Progress entry to a specific Patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Field to store the test result
    result = models.CharField(max_length=50)

    # Timestamp for when the test was taken
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Progress'
        ordering = ['-timestamp'] 