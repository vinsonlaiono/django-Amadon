from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if 'quantity' not in request.session:
        request.session['quantity'] = ''
    if 'product_id' not in request.session:
        request.session['product_id'] = ''
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'price' not in request.session:
        request.session['price'] = 0
    if 'ordered_items' not in request.session:
        request.session['ordered_items'] = 0
    

    return render(request, "first_app/index.html")

def checkout(request):

    context = {
        'cart_total': request.session['total'],
        'price' : request.session['price'],
        'quantity' : request.session['ordered_items']
    }

    return render(request, 'first_app/checkout.html', context)

def buy(request):
    price = 0.0
    quantity = float(request.POST['quantity'])
    if request.POST['product_id'] == 'tshirt':
        price = 19.99 * quantity
    print(request.POST['product_id'])
    if request.POST['product_id'] == 'sweater':
        price = 29.99 * quantity
    if request.POST['product_id'] == 'cup':
        price = 4.99 * quantity
    if request.POST['product_id'] == 'book':
        price = 49.99* quantity
    
    print(price)
    request.session['price'] = price
    request.session['ordered_items'] += quantity
    request.session['total'] += price
    
    print(request.session['total'])
    
    return redirect('/checkout')