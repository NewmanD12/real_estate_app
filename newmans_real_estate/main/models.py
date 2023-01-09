from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 2: 
            errors['fname_error'] = "First name not long enough. Must be at least 2 characters."
        if len(post_data['lname']) < 2: 
            errors['lname_error'] = "Last name not long enough. Must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email_invalid_error'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password_length_error'] = "Password is not long enough! Must be at least 8 characters."
        if post_data['password'] != post_data['confirm_password']: 
            errors['password_match_error'] = "Passwords have to match!"    
        return errors

    def registration_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email_invalid_error'] = "Invalid email address!"
        return errors

class User(models.Model):
  first_name = models.CharField(max_length=254)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'

  objects = UserManager()