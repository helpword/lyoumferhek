from django.urls import path
from .views import SignupView, SignupsuccessView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import (UserDetailView, UserUpdateView, UserListView,
                      change_password,LoginView,UserCreateView,logout_view,
                    UserDeleteView,add_edit_group,
                   RoleDetailView,RoleListView,GroupDeleteView, set_language )
from django.urls import reverse_lazy

app_name= 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name="signup"),
    path('signup_success/', SignupsuccessView.as_view(), name="signup_success"),
    
    path('set_language/<str:language>/', set_language, name="set_language"),
    
    path('users/', login_required(UserListView.as_view()), name="userlist"),
    path('users/detail/<int:pk>', login_required(UserDetailView.as_view()), name="userdetail"),
    path('users/create/', UserCreateView.as_view(), name="user_create_view"),
    path('users/update/<int:pk>/', login_required(UserUpdateView.as_view()), name="edituser"),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete_view'),
    path('users/change_password/<int:pk>/', login_required(change_password), name="change_password"),


    path('logout/', logout_view, name='logout'),

     ###### PASSWORD RESET ##############
    path('password_reset/' , auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name= "registration/password_reset_email.html",
        success_url = reverse_lazy('users:password_reset_done'),), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(
                    template_name='registration/password_change_form.html',
                    success_url = reverse_lazy('users:password_reset_complete'), 
                ), 
                name='password_reset_confirm'),
    path('password_reset/complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


    ###### ROLES ##############
    path('grouplist/', login_required(RoleListView.as_view()), name="grouplist"),
    path("create_role/", add_edit_group, name="create_role"),
    path("edit_role/<int:pk>/", add_edit_group, name="edit_role"),

    path('role_detail/<int:pk>/', RoleDetailView.as_view(), name="role_detail"),
    path("delete_group/<int:pk>/", GroupDeleteView.as_view(), name="delete_group"),

]   