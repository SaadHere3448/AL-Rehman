from django.shortcuts import render, redirect
from buy.models import Order
from django.contrib import messages
from add.models import Product


def AdminProfile(request):
    data = Order.objects.all()
    products = Product.admin.all()
    con = {"data": data, "products": products}
    return render(request, "Dashboard.html", con)


def Fulfil(request, id):
    order = Order.objects.get(id=id)
    order.is_fulfilled = True
    order.save()
    return redirect('/admin-profile/')


def Hide(request, id):
    product = Product.objects.get(id=id)
    product.is_hidden = True
    product.save()
    return redirect('/admin-profile/')


def Display(request, id):
    product = Product.admin.get(id=id)
    product.is_hidden = False
    product.save()
    return redirect('/admin-profile/')


def Update(request, id):
    product = Product.admin.get(id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('product_name')
        price = data.get('price')
        image = request.FILES.get('image')
        category = data.get('category')
        code = data.get('code')
        desc = data.get('description')
        if name:
            already = Product.objects.filter(name=name)
            if already:
                messages.error(request, "Already A Product Has This Name!!!")
                return redirect('/Add-Product/')
        if code:
            already = Product.objects.filter(code=code)
            if already:
                messages.error(request, "Already A Product Has This Code!!!")
                return redirect('/Add-Product/')
        if name:
            product.name = name
        if price:
            product.price = price
        if image:
            product.image = image
        if category:
            product.category = category
        if code:
            product.code = code
        if desc:
            product.description = desc
        product.save()
        messages.info(request, 'Product Updated Successfully!!!')
        return redirect('/admin-profile/')
    return render(request, "Update.html", {"data": product})
