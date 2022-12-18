from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email")
        
        if not first_name:
            raise ValueError("Users must have a first name")
            
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user (
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

# User model with email to login 
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'quesnotion_users'