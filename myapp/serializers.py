from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer): #serializer model object ko json me convert karta hai
  class Meta:
    model = Item
    fields = ["id","item_name","item_desc","item_price","item_image"]