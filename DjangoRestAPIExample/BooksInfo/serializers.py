
from rest_framework import serializers
from .models import Books   #import model
 
# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Books
        fields = '__all__'