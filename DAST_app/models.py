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

class details(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=100,default='default_password')
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.IntegerField()
    employment = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    concern = models.CharField(max_length=100)
    Test_Result=models.CharField(max_length=50)
    class Meta:
        db_table='details'
    
    
    
    

