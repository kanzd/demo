from django.db import models

# Create your models here.

class CodeModel(models.Model):
    id = models.AutoField
    output = models.TextField(max_length=100)
    inputs = models.TextField(max_length=100)
    code = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.id)


    