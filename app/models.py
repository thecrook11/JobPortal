from django.db import models

# Create your models here.


class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.EmailField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=False)
    isCreater = models.DateTimeField(auto_now_add=True)
    isUpdated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    userId = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    minSalary = models.BigIntegerField(default=0)
    maxSalary = models.BigIntegerField(default=0)
    highestEdu = models.CharField(max_length=150, default="")
    jobType = models.CharField(max_length=150, default="")
    jobCategory = models.CharField(max_length=150, default="")
    experience = models.CharField(max_length=150, default="")
    website = models.CharField(max_length=150, default="")
    shift = models.CharField(max_length=150, default="")
    jobDesc = models.CharField(max_length=150, default="")
    profilePic = models.ImageField(upload_to="app/img/candidate")


class Company(models.Model):
    userId = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logoPic = models.ImageField(upload_to="app/img/company")


class JobDetail(models.Model):
    compID = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobName = models.CharField(max_length=250)
    companyName = models.CharField(max_length=250)
    companyAddress = models.CharField(max_length=250)
    jobDescComp = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    responsibilties = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companyWebsite = models.CharField(max_length=250)
    companyEmail = models.CharField(max_length=250)
    companyContact = models.CharField(max_length=20)
    salaryPackage = models.CharField(max_length=250)
    experience = models.IntegerField()
    logoPic = models.ImageField(upload_to="app/company/logo")


class ApplyList(models.Model):
    cand = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    resume = models.FileField(upload_to="app/resume")

class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)