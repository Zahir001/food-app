from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager
from django.utils import timezone
# Create your models here.
class Item(models.Model):
  class Meta:
    indexes = [
      models.Index(fields=['user_name','item_price']),
    ]

  def __str__(self):
    return self.item_name + ":" + str(self.item_price)
  
  def get_absolute_url(self):
    return reverse('myapp:index')
  
  def delete(self,using=None,keep_parents=False):
    self.is_deleted = True
    self.deleted_at = timezone.now()
    self.save()


  user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1) #yani har Item object ek specific user se linked hoga
  item_name = models.CharField(max_length=200,db_index=True)
  item_desc = models.CharField()
  item_price = models.DecimalField(max_digits=6,decimal_places=2,db_index=True)
  # item_image = models.URLField(max_length=500,default='https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg')
  item_image = models.ImageField(upload_to='item_images/',blank=True,null=True)
  is_available = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  is_deleted = models.BooleanField(default=False)#soft delete flag
  deleted_at = models.DateTimeField(null=True,blank=True)#saves timestamp when deleted

  

  objects = ItemManager()
  all_objects = models.Manager()


class Category(models.Model):
  name = models.CharField(max_length=100)
  added_on = models.DateField(auto_now=True)

  def __str__(self):
    return self.name


class Order(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True) #auto_now_add__ye ek hi baar #time genereate kr ke deta hai aur auto_now jo hai har update me time generate kr deta hai 
  items = models.ManyToManyField(Item,related_name='orders')

  def __str__(self):
    return f"Order {self.id} by {self.user.username}"


# NOTE 
# 1 model.objects.all()-> to fetch all rows or items
# 2 model.objects.get(item_name or id ya ...) getting single item
# for multiple item we use filter
# 3 model.objects.filter(item_name or item_price ya ...)
# 4 model.objects.exclude(item_price__lt=5)
# means less than 5 exclude kr do
# 5 model.objects.all().order_by('item_price') to order the item
# 6 model.objects.all().order_by('-item_price') to order the item
# to decending order
# 7 model.objects.values('item_name','item_price')
# to get item in dictionary key and values pairs
# 8 models.objects.count() give total count of items
# 9 model.objects.first()
# give first item and
# model.objects.last()
# give last item from model

# 10 model.objects.filter(item_price__gt=5).exists() gives true or false
# 11 model.objects.filter(item_price__gt=5).count() total no count return

# 12 model.objects.filter(item_name__contains='Burger')
# if no item it DOES NOT GIVE ERROR it give empty query set

# 13 model.objects.filter(item_name__exact='Cheeseburger') it search for exact keyword and it is CASE SENSITIVE
  
# 14 model.objects.filter(item_name__iexact='cheeseburger') it search for exact keyword but it is NOT CASE SENSITIVE

# 15 model.objects.filter(item_price__range=(1,5))

# 16 Item.objects.filter(item_name__startswith='C')

# 17 Item.objects.filter(item_name__endswith='r')

# 18 Item.objects.filter(created_at__year=2026)


# NOTE EXAMPLE DOUBLE FILTER
# 19 Item.objects.filter(item_price__gt=5).filter(item_name__icontains='burger').count() WITH INSENSITIVE

# 20 Item.objects.filter(item_price__gt=5).filter(item_name__contains='burger').count() WITHOUT INSENSITIVE

# 21 Item.objects.aggregate(Sum('item_price')) // django orm method aggregate

# 22 Item.objects.aggregate(Avg('item_price'))

# 23 Item.objects.aggregate(Max('item_price'))

# 24 Item.objects.aggregate(Min('item_price'))

