from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = models.CharField(max_length=150)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,unique=True)
    following = models.ManyToManyField(User,blank=True,related_name='following')
    followers = models.ManyToManyField(User,blank=True,related_name='followers')
    profile_pic = models.ImageField(upload_to='profile_photos',blank=True,default='user.png')

    def __str__(self):
        return self.user.email

class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='posts')
    blog_heading = models.CharField(max_length=150,unique=True)
    blog_content = models.TextField(max_length=2000,unique=True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    uploaded_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username