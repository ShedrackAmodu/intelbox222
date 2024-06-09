from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm 
from django.contrib.auth.decorators import login_required
from storefront.models import Product as StorefrontProduct 
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = StorefrontProduct.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        products = StorefrontProduct.objects.all()
   # products = StorefrontProduct.objects.all()  #used the storefront so it shows update time and created time 
    # also the admin is for the owner and trustees and user end has it for the employees interface as the outside world
    #have limited views but same app also 
    return render(request, 'storeadmin/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'storeadmin/add_product.html', {'form': form})

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'storeadmin/edit_product.html', {'form': form})

def delete_product(request, pk):
    delete = False
    try:#for   admin   data/products
        product = Product.objects.get(pk=pk)
        if request.method == 'POST':
            product.delete()
            delete = True
    except :
        pass
    try:#for  front data/products
        if delete:
            frontproducts = StorefrontProduct.objects.get(pk=pk)
            frontproducts.delete()
        return redirect('product_list')
    except :
        pass
    
    return render(request, 'storeadmin/delete_product.html', {'product': product})

 

#def admin_update_product(request, product_id):
#    product = get_object_or_404(Product, id=product_id)
#    if request.method == 'POST':
#        stock = request.POST.get('stock')
#        if stock:
#            product.stock = stock
#            product.updated_at = timezone.now()
#            product.save()
#            return redirect('storeadmin/product_list')
#    return render(request, 'storeadmin/edit_product.html', {'product': product})