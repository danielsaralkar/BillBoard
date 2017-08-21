from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Messages(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return self.title