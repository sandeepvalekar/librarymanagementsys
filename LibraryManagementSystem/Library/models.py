from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
 user=models.OneToOneField(User,on_delete=models.CASCADE)
enrollment = models.CharField(max_length=40)
branch = models.CharField(max_length=40)


class Book(models.Model):
    Catchoice=[
      ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),]

    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=Catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'

        def get_expiry():
         return datetime.today() + timedelta(days=15)
  
    class Meta:
      db_table="book"