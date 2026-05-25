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

  def clean_item_price(self):
    price = self.cleaned_data["item_price"]
    if price<0:
        print("zahiralamsitamarhi")
        raise forms.ValidationError("Price cannot be negative")
    return price
  

  def clean(self):
     cleaned = super().clean()
     name = cleaned.get("item_name")
     desc = cleaned.get("item_desc")
     if name and desc and name.lower() == desc.lower():
        self.add_error("item_desc","Description should be not same as item name")

     if len(desc) < 15:
        self.add_error("item_desc", "Description is Too short")

     return cleaned
