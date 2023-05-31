from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.indexPage,name="index"),
    path("signup/",views.signupPage,name="signup"),
    path("register/",views.registerUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.OTPVerify,name="otp"),
    path("loginpage/",views.loginPage,name="loginpage"),
    path("loginuser/",views.loginUser,name="login"),
    path("profile/<int:pk>",views.profilePage,name="profile"),
    path("updateprofile/<int:pk>",views.updateProfile, name="updateprofile"),
    path("logut/",views.logutUser,name="logut"),
    path("joblistpage/",views.CandidateJobList,name="joblistpage"),
    path("applyjobpage/<int:pk>",views.ApplyJobPage,name="applyjobpage"),
    path("applyjob/<int:pk>",views.applyJob,name="apply"),
    path("about/",views.AboutUsPage,name="about"),
    path("contact/",views.ContactUsPage,name="contact"),
    path("contactus/",views.contact,name="contactus"),
##########################Company Side##################################################
    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.updateCompanyProfile,name="updatecompanyprofile"),
    path("jobpostpage/",views.jobPostPage,name="jobpostpage"),
    path("jobpost/",views.jobDetailSubmit,name="jobpost"),
    path("jobpostlist/",views.jobPostList,name="joppostlist"),
    path("applylist/",views.applyJobList,name="applylist"),
    
    
##########################ADMIN SIDE#############################################################3

    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminindexpage",views.AdminIndexPage,name="adminindex"),
    path("adminlogin/",views.adminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="adminuserlist"),
    path("admincompanylist/",views.AdminCompanyList,name="admincompanylist"),
    path("userdelete/<int:pk>",views.UserDelete,name="userdelete"),
    path("verifypage/<int:pk>",views.VerifyPage,name="verifypage"),
    path("companyverify/<int:pk>",views.CompanyVerify,name="companyverify"),
    path("compdelete/<int:pk>",views.CompDelete,name="compdelete"),
    path("logutadmin/",views.LogutAdmin,name="logutadmin")
  
]