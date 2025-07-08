from django.shortcuts import render, redirect
from django.contrib import messages
from add.models import Product


def Add_Product(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('product_name')
        price = data.get('price')
        image = request.FILES.get('image')
        category = data.get('category')
        code = data.get('code')
        desc = data.get('description')
        already = Product.objects.filter(name=name)
        if already:
            messages.error(request, "Already A Product Has This Name!!!")
            return redirect('/Add-Product/')
        already = Product.objects.filter(code=code)
        if already:
            messages.error(request, "Already A Product Has This Code!!!")
            return redirect('/Add-Product/')
        product = Product.objects.create(
            name=name,
            code=code,
            image=image,
            price=price,
            category=category,
            description=desc
        )
        product.save()
        messages.info(request, 'Product Added Successfully!!!')
        return redirect('/Add-Product/')
    return render(request, "Add-Product.html")
