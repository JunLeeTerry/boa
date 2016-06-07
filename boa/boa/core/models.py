from django.db import models

# Create your models here.
class Answer(models.Model):
    chanswer = models.CharField(max_length=200,blank=False)
    enanswer = models.CharField(max_length=400,blank=False)

    def __str__(self):
        return str(self.id)


