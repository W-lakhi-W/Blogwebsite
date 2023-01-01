"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sign_up_view,name='sign_up'),
    path('login',views.login_view,name='login_view'),
    path('logout',views.logout_view,name='logout'),
    path('"/"',views.home_view,name='home_view'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('upload_blog',views.post_view,name='blog_post_view'),
    path('follow/<int:id>',views.follow_view,name='follow'),
    path('like/<int:id>',views.like_view,name='like'),
    path('search',views.search_view,name='search_view'),
    path('show/<int:id>',views.show_blog,name="show_blog"),
    path('change_photo',views.change_photo_view,name="change_photo"),
    #path('logout',LogoutView.as_view(next_page=settings.REDIRECT_URL),name='logout'),

    # password reset urls #
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    
] 

urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


