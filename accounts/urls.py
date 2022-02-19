from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_view, name="users"),
    path('users/create', views.create_account, name="create users"),
    path('users/reset_password', views.reset_password, name="reset password"),
    path('auth/', views.login_view, name="login"),
    path('auth/forgot_password', views.forgot_password, name="forgot password"),
    path('auth/verify_otp_password', views.verify_otp_pass, name="verify otp change pass"),
    path('users/profile/', views.profile_view, name="profile"),
    path("users/verify_otp/", views.verify_otp),
    path("users/new_otp/", views.new_otp),
    path("blog/create_post/", views.create_post),
    path("blog/get_posts/", views.get_posts),
    path("blog/post_detail/<int:post_id>/", views.post_detail),
    path("blog/create_like/", views.create_like),
    path("blog/view_likes/", views.view_likes),
    path("blog/view_likers/<int:post_id>", views.view_likers),
    
]