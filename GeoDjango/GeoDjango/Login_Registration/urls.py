from django.urls import path
from .import views
from .forms import PasswordReset
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView 

                                        

urlpatterns=[
    path('register/', views.signup_view, name='signup_url'),
    path('login/', views.login_view, name='login_url'),
    path('otp/',views.otpLogin, name="otp-login-url"),
    path('logout/', views.logout_view, name='logout_url'),
    path('account-verify/<slug:token>', views.account_verify, name='account-verify'),

    #Reset Password
    path('reset-password/', PasswordResetView.as_view(template_name='Login&Register/resetpassword.html'), name='reset-password'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='Login&Register/reset-password-confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='Login&Register/reset-password-done.html'), name='password_reset_done'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='Login&Register/password-reset-complete.html'), name='password_reset_complete'),

    #Change Password
    path('change-password/', PasswordChangeView.as_view(template_name='Login&Register/changepassword.html'), name='password_change_url'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='Login&Register/change-password-done.html'), name='password_change_done'),
    
    #change profile.
    path('edit-profile/', views.ProfileChangeView, name='edit_profile_url'),

    

      
]
