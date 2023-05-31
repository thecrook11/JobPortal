from django.shortcuts import render, redirect
from .models import *
from random import randint

# Create your views here.


def indexPage(request):
    return render(request, "apps/user/index.html")


def signupPage(request):
    return render(request, "apps/user/signup.html")


def registerUser(request):
    if request.POST['role'] == 'Candidate':
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "User already exist!"
            return render(request, "apps/user/signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = int(randint(100000, 999999))
                newUser = UserMaster.objects.create(
                    role=role, otp=otp, email=email, password=password)
                newCand = Candidate.objects.create(
                    userId=newUser, fname=fname, lname=lname)
                return render(request, "apps/user/otpverify.html", {'email': email})
            else:
                message = "Password & Confirm Password Does not Match!"
                return render(request, "apps/user/signup.html", {'msg': message})
    else:
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "Company already exist!"
            return render(request, "apps/user/signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = int(randint(100000, 999999))
                newUser = UserMaster.objects.create(
                    role=role, otp=otp, email=email, password=password)
                newComp = Company.objects.create(
                    userId=newUser, fname=fname, lname=lname)
                return render(request, "apps/user/otpverify.html", {'email': email})
            else:
                message = "Password & Confirm Password Does not Match!"
                return render(request, "apps/user/signup.html", {'msg': message})


def OTPPage(request):
    return render(request, "apps/user/otpverify.html")


def OTPVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "OTP Verified Successfully!"
            return render(request, "apps/user/login.html", {'msg': message})
        else:
            message = "OTP Is Invalid!"
            return render(request, "apps/user/otpverify.html", {'msg': message})
    else:
        return render(request, "apps/user/signup.html")


def loginPage(request):
    return render(request, "apps/user/login.html")


def loginUser(request):
    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password == password and user.role == "Candidate":
                cand = Candidate.objects.get(userId=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['fname'] = cand.fname
                request.session['lname'] = cand.lname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('index')
            else:
                message = "Password does not Match!"
                return render(request, "apps/user/login.html", {'msg': message})
        else:
            message = "User does not Exist!"
            return render(request, "apps/user/login.html", {'msg': message})
    else:
        if request.POST['role'] == "Company":
            email = request.POST['email']
            password = request.POST['password']
            user = UserMaster.objects.get(email=email)
            if user:
                if user.password == password and user.role == "Company":
                    comp = Company.objects.get(userId=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['fname'] = comp.fname
                    request.session['lname'] = comp.lname
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('companyindex')
                else:
                    message = "Password does not Match!"
                    return render(request, "apps/user/login.html", {'msg': message})
            else:
                message = "User does not Exist!"
                return render(request, "apps/user/login.html", {'msg': message})


def profilePage(request, pk):
    user = UserMaster.objects.get(pk=pk)
    cand = Candidate.objects.get(userId=user)
    return render(request, "apps/user/profile.html", {'user': user, 'cand': cand})


def updateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        cand = Candidate.objects.get(userId=user)
        cand.state = request.POST['state']
        cand.city = request.POST['city']
        cand.country = request.POST['country']
        cand.address = request.POST['address']
        cand.jobType = request.POST['jobType']
        cand.jobCategory = request.POST['jobCategory']
        cand.jobDesc = request.POST['jobDesc']
        cand.minSalary = request.POST['minSalary']
        cand.maxSalary = request.POST['maxSalary']
        cand.contact = request.POST['contact']
        cand.experience = request.POST['experience']
        cand.highestEdu = request.POST['highestEdu']
        cand.dob = request.POST['dob']
        cand.shift = request.POST['shift']
        cand.website = request.POST['website']
        cand.gender = request.POST['gender']
        cand.profilePic = request.FILES['profilePic']
        cand.save()
        url = f"/profile/{pk}"
        return redirect(url)


def logutUser(request):
    del request.session['email']
    del request.session['password']
    del request.session['fname']
    del request.session['lname']
    return redirect('index')


def CandidateJobList(request):
    allJobs = JobDetail.objects.all()
    return render(request, "apps/user/job-list.html", {'allJobs': allJobs})


def ApplyJobPage(request, pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(userId=user)
        job = JobDetail.objects.get(id=pk)
    return render(request, "apps/user/apply.html", {'user': user, 'cand': cand, 'job': job})


def applyJob(request, pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(userId=user)
        job = JobDetail.objects.get(id=pk)
        edu = request.POST['qualification']
        website = request.POST['website']
        exp = request.POST['experience']
        resume = request.FILES['resume']
        newApply = ApplyList.objects.create(
            cand=cand, job=job, qualification=edu, website=website, experience=exp, resume=resume)
        message = "Job applied successfully!"
        return render(request, "apps/user/apply.html", {'msg': message})
########################## Company Side#############################################


def CompanyIndexPage(request):
    return render(request, "apps/company/index.html")


def CompanyProfilePage(request, pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(userId=user)
    return render(request, "apps/company/profile.html", {'user': user, 'comp': comp})


def updateCompanyProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(userId=user)
        comp.companyName = request.POST['companyName']
        comp.country = request.POST['country']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.address = request.POST['address']
        comp.logoPic = request.FILES['logoPic']
        comp.save()
        url = f"/companyprofile/{pk}"
        return redirect(url)


def jobPostPage(request):
    return render(request, "apps/company/jobpost.html")


def jobDetailSubmit(request):
    user = UserMaster.objects.get(id=request.session['id'])

    if user.role == "Company":
        comp = Company.objects.get(userId=user)
        jobName = request.POST['jobName']
        companyName = request.POST['companyName']
        companyAddress = request.POST['companyAddress']
        jobDesc = request.POST['jobDesc']
        qualification = request.POST['qualification']
        responsibilties = request.POST['responsibilties']
        location = request.POST['location']
        companyWebsite = request.POST['companyWebsite']
        companyEmail = request.POST['companyEmail']
        companyContact = request.POST['companyContact']
        salaryPackage = request.POST['salaryPackage']
        experience = request.POST['experience']
        logoPic = request.FILES['logoPic']

        newJob = JobDetail.objects.create(compID=comp, jobName=jobName, companyName=companyName,
                                          companyAddress=companyAddress, jobDescComp=jobDesc, qualification=qualification, responsibilties=responsibilties,
                                          location=location, companyWebsite=companyWebsite, companyEmail=companyEmail, companyContact=companyContact,
                                          salaryPackage=salaryPackage, experience=experience, logoPic=logoPic)

        message = "JOB Post Successfully!"
        return render(request, "apps/company/jobpost.html", {'msg': message})


def jobPostList(request):
    allJobs = JobDetail.objects.all()

    return render(request, "apps/company/jobpostlist.html", {'allJobs': allJobs})


def applyJobList(request):
    allJobs = ApplyList.objects.all()
    user = UserMaster.objects.all()
    return render(request, "apps/company/applyjoblist.html", {'allJobs': allJobs, 'user': user})
# ADMIN SIDE######################################################################3


def AdminLoginPage(request):
    return render(request, "apps/admin/login.html")


def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request, "apps/admin/index.html")
    else:
        return redirect('adminloginpage')


def adminLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == 'admin':
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')


def AdminUserList(request):
    user = UserMaster.objects.filter(role="Candidate")

    return render(request, "apps/admin/userlist.html", {'user': user})


def AdminCompanyList(request):
    user = UserMaster.objects.filter(role="Company")

    return render(request, "apps/admin/companylist.html", {'user': user})


def UserDelete(request, pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('adminuserlist')


def VerifyPage(request, pk):
    comp = UserMaster.objects.get(pk=pk)
    if comp:
        return render(request, "apps/admin/verify.html", {'comp': comp})


def CompanyVerify(request, pk):
    comp = UserMaster.objects.get(pk=pk)
    if comp:
        verify = request.POST['isVerified']
        comp.isVerified = verify
        comp.save()
        return redirect("admincompanylist")


def CompDelete(request, pk):
    comp = UserMaster.objects.get(pk=pk)
    comp.delete()
    return redirect('admincompanylist')


def LogutAdmin(request):
    del request.session['username']
    del request.session['password']
    return redirect("adminloginpage")


def AboutUsPage(request):
    return render(request, "apps/user/about.html")


def ContactUsPage(request):
    return render(request, "apps/user/contact.html")


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        msg = request.POST['msg']

        newContact = Contact.objects.create(
            fname=fname, lname=lname, email=email, msg=msg)
        message = "Message Sent Successfully!"
        return render(request, "apps/user/contact.html", {'message': message})
