from . import models
from rest_framework import serializers

class CodeSerializers(serializers.ModelSerializer):
    class Meta:
         fields = '__all__'
         model = models.CodeModel
