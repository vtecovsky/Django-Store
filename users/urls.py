from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from django.urls import path, reverse_lazy

from users.views import (EmailVerificationView,
                         UserLoginView, UserProfileView, UserRegistrationView)

app_name = "users"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile<int:pk>/", login_required(UserProfileView.as_view()), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "verify/<str:email>/<uuid:code>/",
        EmailVerificationView.as_view(),
        name="email_verification",
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done'),
                                                                 template_name="users/password_reset.html"),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
         name='password_reset_done',
         ),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete'),
                                                     template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
]
