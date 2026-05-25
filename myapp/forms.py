from django import forms
from .models import Item
class ItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    widgets = {
        "item_name":forms.TextInput(attrs={"placeholder":"e.g Margherita Pizza","required":True,"class":"w-full"}),
        "item_desc":forms.TextInput(attrs={"placeholder":"e.g Fresh Cheese","required":True,"class":"w-full"}),
        "item_price":forms.NumberInput(attrs={"placeholder":"e.g 100","required":True,"class":"w-full"}),
        "item_image":forms.URLInput(attrs={"placeholder":"https://www.google.com","required":False,"class":"w-full"}),
    }