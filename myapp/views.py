from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
# @login_required
# @cache_page(60 * 15)
# @vary_on_headers("Agent-User") #Agent-User is case sensitive

logger = logging.getLogger(__name__)

def index(request):
  logger.info("Fetching all items from the database")
  logger.info(f"User{request.user} at {timezone.now()} time requested item list from {request.META.get('REMOTE_ADDR')} address")
  item_list = Item.objects.all()
  logger.debug(f"found {item_list.count()} items")
  paginator = Paginator(item_list,5)
  page_number = request.GET.get('page') #request.GET se page no nika rha hia
  page_obj = paginator.get_page(page_number)
  print('pagggee-obj',page_obj)
  # return HttpResponse(item_list)
  context = {
    'page_obj':page_obj
  }
  print('paaggee__objj',list(page_obj)) 
  return render(request,"myapp/index.html",context)

# class IndexClassView(LoginRequiredMixin,ListView):
#   model = Item
#   template_name = 'myapp/index.html'
#   context_object_name = 'item_list'


def detail(request, id):
  logger.info(f"Fetching an item with id:{id}")
  try:
      item = get_object_or_404(Item,pk=id) #isse item v milega aur error v check krega isiliye niche wala code comment kr diya
      # item = Item.  objects.get(id=id)
      logger.debug(f"Item found {item.item_name} $({item.item_price})")
  except Exception as e:
      logger.error(f"Error fetching the item with id {id},{e}")
      raise
  context = {
    "item":item
  }
  return render(request,"myapp/detail.html",context)
  # return HttpResponse(f"This is detail view with id:{id}")

# class FoodDetailView(DetailView):
#   model = Item
#   template_name = 'myapp/detail.html'
#   context_object_name = 'item'
  


def create_item(request):
  form = ItemForm(request.POST or None)
  if request.method=="POST":
    # form = ItemForm(request.POST)  # print(request.POST) # form se submitted data nikalne ke liye request.post
    if form.is_valid():
        form.save()
        return redirect('myapp:index')


  context ={
    'form':form
  }
  return render(request,'myapp/item-form.html',context)

# class ItemCreateView(CreateView):
#   model = Item
#   fields = ['item_name','item_desc','item_price','item_image']
#   def form_valid(self, form):
#     # form object createview khud bna leta hai internally
#     form.instance.user_name = self.request.user #request.user = gives current loggedin user and form.instanace = full object of Item model Class
#     # user_name is a ForeignKey field.
#     # It does not store plain string/text.
#     # It stores reference(id) of a User object from another table.
    
#     return super().form_valid(form)
  
# SHORT NOTE
# form = Form(request.POST)
# form.instance = model object
# form_valid() = called after validation
# super().form_valid(form) = saves object
# SHORT NOTE TO REMEMBER

#create view automatically modelname_form template dhundhta hai jo ki ham 
#create kar chuke hai usme ham form render kra dete hai model ke field ka help se
# aur form submit hone pe automatically db me save v ho jata hai 




# def update_item(request,id):
#   item = Item.objects.get(id=id)
#   form = ItemForm(request.POST or None,instance=item)
#   if form.is_valid():
#     form.save()
#     return redirect('myapp:index')

#   context = {
#     'form':form
#   }
#   return render(request,'myapp/item-form.html',context)

class ItemUpdateView(UpdateView):
  model = Item
  # fields = ['item_name','item_desc','item_price','item_image']
  form_class = ItemForm # upar wala v use ho sakta hai ye wala ItemForm se 
  #validation lena ttha isiliye likha "FORM_CLASS" ye inbuilt keyword hai django ka
  template_name_suffix = '_update_form'

  def get_queryset(self):
    return Item.objects.filter(user_name=self.request.user)


# def delete_item(request,id):
#   item = Item.objects.get(id=id)
#   if request.method=='POST':
#     item.delete()
#     return redirect('myapp:index')
  
#   return render(request,'myapp/item-delete.html')

class ItemDeleteView(DeleteView):
  model = Item
  success_url = reverse_lazy('myapp:index')