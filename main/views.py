from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View
from .models import *

from main.forms import *


class ProductsView(View):
    def get(self,request, id=0):
        if id == 0:
            form = ProductsForm()
        else:
            products = Products.objects.get(pk=id)
            form = ProductsForm(instance=products)
        return render(request, 'main/products_form.html',{'form':form})

    def post(self,request, id=0):
        sku = request.POST['sku']
        if id == 0:
           form = ProductsForm(request.POST)
        else:
            products = Products.objects.get(pk=id)
            form = ProductsForm(request.POST,instance=products)
        if form.is_valid():
            messages.success(request, "Registered Successfully")
            form.save()
        elif Products.objects.filter(sku=sku).exists():
            messages.error(request,"sku already exists" + sku)
        return redirect('/products_list')

class Products_list(View):
  def get(self,request):
    list = Products.objects.all()
    return render(request, 'main/products_list.html',{'list':list})
  def post(self,request,*args,**kwargs):
      if request.method=="POST":
          product_ids =request.POST.getlist('id[]')
          for id in product_ids:
              product = Products.objects.get(pk=id)
              product.delete()
          return redirect('/products_list')


