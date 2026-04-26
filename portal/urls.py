from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('auth/', views.auth_page, name='auth'),

    # LOGIN
    path('login/', auth_views.LoginView.as_view(
        template_name='portal/auth.html'
    ), name='login'),

    # LOGOUT
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # SIGNUP
    path('signup/', views.signup, name='signup'),

    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='portal/forgot_password.html',
            email_template_name='portal/password_reset_email.html',
            success_url='/forgot-password/done/'
        ),
        name='forgot_password'
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='portal/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='portal/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='portal/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/<int:id>/', views.organization_detail, name='organization_detail'),

    path('departments/<int:id>/', views.department_detail, name='department_detail'),
    path('teams/<int:id>/', views.team_detail, name='team_detail'),
]