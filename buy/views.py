from django.shortcuts import render, redirect
from django.contrib import messages
from buy.models import Order


def Buy(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('fullName')
        phone = data.get('phone')
        email = data.get('email')
        address = data.get('address')
        city = data.get('city')
        place = data.get('place')
        notes = data.get('notes')
        order = Order.objects.create(
            cus_name=name,
            cus_phone=phone,
            cus_email=email,
            cus_address=address,
            cus_city=city,
            cus_place=place,
            cus_notes=notes
        )
        order.save()
        messages.success(request, "Ordered Successfully!!!")
        return redirect('/buy/')
    return render(request, "Buy.html")
