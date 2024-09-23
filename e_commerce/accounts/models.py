from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from product.models import Product
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

# User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True  # Ensure superuser is marked as staff
        user.is_superuser = True  # Ensure superuser has all permissions
        user.save(using=self._db)
        return user

# User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Staff can access the admin site
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_images/')  # Define where images will be uploaded
    prefer = models.ManyToManyField(Product, blank=True)  # Allow empty preferences
    join_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(default="01000000000",null=True,blank=True,validators=[MinLengthValidator(10), MaxLengthValidator(11)])
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True  # Adjust as per your permission system

    def has_module_perms(self, app_label):
        return True 
    # @property 
    # def is_staff(self):
    #     return self.is_admin
    