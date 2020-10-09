from django.db import models

# Create your models here.
class Client(models.Model):
    def __str__(self):
        return self.cname

    cname = models.CharField(max_length=20,unique=True)
    cgender = models.CharField(max_length=10, choices=(('male','男'), ('female','女')),default='male', verbose_name='性别')
    cage = models.IntegerField()
    cemail = models.EmailField()
    cphonenum = models.CharField(max_length=20)
    cpasswords = models.CharField(max_length=100,default=None)
    # clevel = models.BooleanField(default=False)

class Manager(models.Model):
    def __str__(self):
        return self.mname

    mname = models.CharField(max_length=20,unique=True)
    # mgender = models.CharField(max_length=10, choices=(('male','男'), ('female','女')),default='male', verbose_name='性别')
    # mage = models.IntegerField()
    # memail = models.CharField(max_length=100)
    # mphonenum = models.CharField(max_length=20)
    mpasswords = models.CharField(max_length=100,default=None)

