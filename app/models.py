from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def check_for_p(value):
    if value[0].lower()=='p':
        raise ValidationError('started with p')



class Topic(models.Model):
    topic_name=models.CharField(max_length=100,validators=[check_for_p])

    def __str__(self):
        return self.topic_name