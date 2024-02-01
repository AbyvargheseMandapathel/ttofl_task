from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError()
        user = self.model(email= self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password):
        user = self.create_user(email=email,password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
               

class Author(AbstractBaseUser,PermissionsMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique = True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='authors/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    id = models.CharField(unique=True,max_length=20,primary_key=True)


    USERNAME_FIELD = 'email'
    objects = UserManager()

    def generate_author_id(self):
        if not self.id and not self.is_superuser:
            city_code = self.city[:3].upper()
            last_author = Author.objects.filter(city=self.city, is_superuser=False).order_by('-id').first()
            if last_author:
                last_id = int(last_author.id[-4:]) + 1
            else:
                last_id = 1
            self.id = f'AR{city_code}{last_id:04d}'

    def save(self, *args, **kwargs):
        self.generate_author_id()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email