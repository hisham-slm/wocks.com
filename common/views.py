from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import F
from common.models import Cart, Customer, Review
from django.core.mail import send_mail

from wocks_admin.models import Product, Size
from .decorators import auth_customer

from django.views.decorators.cache import cache_control

# Create your views here.


def home_page(request):
    return render(request, 'cust_temp/home_page.html')


def login_page(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email=email, password=password)
            request.session['customer'] = customer.id
            return redirect('customer:shoespage')

        except:
            msg = "Invalid Email or Password"

    return render(request, 'cust_temp/login.html', {'msg': msg})


def signup_page(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        new_customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        msg = "Welcome to Wocks Sneaks" + " " + first_name + " " + last_name + \
            " We Wish you a happy shopping \n\nregards: Wocks sneaks"

        send_mail("Lets Get some sneakers",
                  msg,
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently=False
                  )
        new_customer.save()
        return redirect('customer:login')
    return render(request, 'cust_temp/signup.html')


@auth_customer
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def shoes(request):
    products = Product.objects.filter(category='Shoes')
    return render(request, 'cust_temp/shoes.html', {'products': products})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@auth_customer
def prod_details(request, pid):
    product = Product.objects.get(id=pid)
    review = Review.objects.all()
    context = {
        'product': product,
        'review' : review
    }
    return render(request, 'cust_temp/prod_desc.html', context)


def email_exist(request):
    email = request.POST['email']
    status = Customer.objects.filter(email=email).exists()
    return JsonResponse({'status': status})


def logout(request):
    del request.session['customer']

    request.session.flush()

    return redirect('customer:home_page')


@auth_customer
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def watches(request):
    products = Product.objects.filter(category='Watches')
    return render(request, 'cust_temp/watches.html', {'products': products})


@auth_customer
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_to_cart(request):
    return render(request, 'cust_temp/add_to_cart.html')


def review(request, pid):
    if request.method == 'POST':
        comment = request.POST['comment']
        customer_id = Customer.objects.get(id = request.session['customer'])
        product_id = Product.objects.get(id = pid)

        new_review = Review(
            comment=comment,
            customer_id=customer_id,
            product_id=product_id
        )

        new_review.save()

        review = Review.objects.filter(id = pid)

    return render(request, 'cust_temp/prod_desc.html', {'review': review})
@auth_customer
def cart(request):
    cart_data = Cart.objects.filter(customer_id=request.session['customer']).annotate(total = F('product__prod_price')*F('quantity'))
    size = Size.objects.all()
    # cart_data = Cart.objects.annotate(total = F('product__prod_price')*F('quantity'))
    grand_total = 0
    for products in cart_data:
        grand_total = products.total + grand_total
    request.session['grand_total'] = grand_total

    context = {
        'cart_data': cart_data,
        'grand_total' : grand_total,
        'size':size
    }

    return render (request, 'customer_temp\cart.html',context)