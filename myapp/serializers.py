from rest_framework import serializers
from .models import Item,Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id","username","email"]


class ItemSerializer(serializers.ModelSerializer): #serializer model object ko json me convert karta hai
  user_name = UserSerializer(read_only=True) #ye bas output ke liye input nhi lega user se kyuki read only hai matlab request me ham user_name boyd me nhi bhej sakte 
  class Meta:
    model = Item
    fields = ["id","user_name","item_name","item_desc","item_price","item_image"]
  
  def validate_item_price(self,value): #field level validation syntax validate_field name
    if value<0:
      raise serializers.ValidationError("Price cant be negative or zero")
    return value
  
  def validate(self,data): #here data is complete object of Item model
    if data["item_name"].lower() == data["item_desc"].lower():
      raise serializers.ValidationError("Item name and Item description cannot be the same")
    elif len(data["item_desc"])<15:
      raise serializers.ValidationError("Item description is too short")
    return data


class OrderSerializer(serializers.ModelSerializer):
  items = ItemSerializer(many=True,read_only=True) # nested item data show karega, only output sara item ko readable json format me
  user = serializers.StringRelatedField() # readable string output (__str__), not for input
  class Meta:
    model = Order
    fields = ["id","user","created_at","items"]

#nested api set bydefault to read only