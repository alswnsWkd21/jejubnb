from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
  	return render(request, 'product/index.html')

def product(request):
  	productlist = Product.objects.all()
  	return render(request, 'product/product.html', {'productlist':productlist,})