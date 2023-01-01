from django.shortcuts import render,redirect
from myapp.models import User,Profile,BlogPost
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,logout ,authenticate
from django.views.decorators.cache import cache_control
from django.db.models import Count
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
import os
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('sign_up')
            else:
                profile1 = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                profile1.save()
                messages.info(request,'user created successfully')

                profile2 = Profile.objects.create(user=profile1,name=username)
                profile2.save()

                user = authenticate(email=email,password=password1)

                if user is not None:
                    login(request,user)
                    return redirect('home_view')
                
                return redirect('login')
        else:
            messages.info(request,'passwords are not matched')
            return render(request,'user_register.html')
    else:
        return render(request,'user_register.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
            
        user = authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('home_view')
        else:
            messages.error(request,'Invalid password/email')
            return redirect('login_view')
    else:
        return render(request,'user_login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def logout_view(request):
    request.session.flush()
    request.user=AnonymousUser()
    return redirect('login_view')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
@login_required(login_url='login_view')
def home_view(request):
    data = BlogPost.objects.all()
    current_user = Profile.objects.get_or_create(user=request.user)
    return render(request,'home.html',{'data':data,'current_user':current_user})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def profile(request,id):
    if request.user.id == id:
        user_profile = Profile.objects.get(id=request.user.id)
        total_posts = BlogPost.objects.filter(user=request.user.id)
        return render(request,'profile.html',{'profile':user_profile,'total_posts':total_posts.count(),'all_posts':total_posts})

    else:
        user_profile = Profile.objects.get(user=id)
        total_posts = BlogPost.objects.filter(user=id)
        return render(request,'profile.html',{'profile':user_profile,'total_posts':total_posts.count(),'all_posts':total_posts})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def like_view(request,id):
    if request.method == 'POST':
        blog_post = BlogPost.objects.get(blog_id=id)
        profile = Profile.objects.get(user = request.user.id)
        post_like = 'Unlike'
        if request.user in blog_post.likes.all():
            blog_post.likes.remove(profile.user.id)
            post_like = 'Unlike'
        else:
            blog_post.likes.add(profile.user.id)
            post_like = 'Like'
        
        data = {
            'value' : post_like,
            'total_likes': blog_post.likes.all().count()
        }

        return JsonResponse(data,safe=False)
            

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def follow_view(request,id):
    if request.user.id == id:
        redirect('home_view')
    if request.method == 'POST':
        login_profile = Profile.objects.get(user=request.user)
        follow_profile = Profile.objects.get(user=id)
        if request.user in follow_profile.followers.all():
            follow_profile.followers.remove(login_profile.user.id)
            login_profile.following.remove(follow_profile.user.id)
            return redirect('home_view')
        else:
            login_profile.following.add(follow_profile.user.id)
            follow_profile.followers.add(login_profile.user.id)
            
            return redirect('home_view')
    return redirect('home_view')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def post_view(request):
    if request.method == 'POST':
        blog_heading = request.POST['blog_heading']
        blog_image = request.FILES['blog_pic']
        blog_content = request.POST['blog_content']
        prof = Profile.objects.get(user=request.user)
        data = BlogPost.objects.create(user = request.user,image=blog_image,blog_heading=blog_heading,blog_content=blog_content,profile=prof)
        data.save()
        return redirect('blog_post_view')
    else:
        return render(request,'upload_blog.html')



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def search_view(request):
    try:
        search_word = request.GET['search']
        search_result = BlogPost.objects.filter(blog_heading__startswith=search_word)
        return render(request,'search.html',{'search_result':search_result})
    except:
        return redirect('home_view')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def show_blog(request,id):
    blog = BlogPost.objects.filter(blog_id = id)
    return render(request,'blog_view.html',{'blog':blog})



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login_view')
def change_photo_view(request):
    if request.method == 'POST':
        photo = request.FILES['photo_user']
        user_profile = Profile.objects.get(user=request.user)
        try:
            os.remove(user_profile.profile_pic.path)
        except Exception as e:
            print("Exeption in removing old profile pic ", e)
        user_profile.profile_pic = photo
        user_profile.save()
        return redirect('profile/{}'.format(request.user.id))

    else:
        return render(request,'change_photo.html')