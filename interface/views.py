from django.shortcuts import render
from interface.models import Storage
from add.models import Product


def interface(request):
    logo = Storage.objects.all()
    pros = Product.objects.all()
    con = {"logo": logo, "products": pros}
    return render(request, "Interface.html", con)


def Fill_Storage(request):
    if request.method == 'POST':
        data = request.FILES.get('image')
        store = Storage.objects.create(
            image=data
        )
        store.save()
    return render(request, "Fill-Storage.html")
