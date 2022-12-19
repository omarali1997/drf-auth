from .models import Snack
from rest_framework import serializers

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        # fields = '__all__'
        fields = ['id','title','purchaser','description']

