
# Create your models here.

from django.db import models
 
 
 
 
# Entry some data into model

class Mir(models.Model):
    ip = models.CharField(max_length=128)
    userid = models.IntegerField()
    currentstate = models.CharField(max_length=20)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
   
    class Meta:
        managed = False
        db_table = 'mir'

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Books(models.Model):
    book_name = models.CharField(max_length=10)
    author_name = models.CharField(max_length=10)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
 
# Create a string representation
    def __str__(self):
        return self.book_name