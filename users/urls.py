from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout", views.close_session, name="logout"),
    path("social/signup/", views.redirect_signin_with_google, name="signup_redirect"),
    path("social/login/cancelled/", views.redirect_signin_whith_google_cancel,
         name="signin_cancel_redirect"),

    # SEND EMAIL FOR RESET USER PASSWORD
    path("send_email", views.forgot_password, name="forgot_password"),
    # VALIDATE EMAIL, TOKEN FOR THE NEXT STEP
    path("reset_password_validate/<uidb64>/<token>",
         views.reset_password_validate, name="reset_password_validate"),
    # CONFIRM AND APPLIED THE NEW PASSWORN ON ACCOUNT
    path("reset_password_confirm", views.reset_password_confirm,
         name="reset_password_confirm"),

    path('settings/', views.settings_view, name='settings_view'),
    path('delete_account/', views.delete_account, name='delete_account')
]
