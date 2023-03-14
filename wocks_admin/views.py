from django.shortcuts import render,redirect

from wocks_admin.models import Admin, Product, Variants
from wocks_admin.decorators import auth_admin
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@auth_admin
def admin(request):
    product = Product.objects.all()
    return render(request, 'admin_temp/admin_home.html',{'products':product})


def admin_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            admin = Admin.objects.get(username = username, password = password)
            request.session['admin'] = admin.id
            return redirect('admin:admin_home')
        except:
            msg = 'Invalid Username or Password'
    return render(request, 'admin_temp/admin_login.html',{'msg':msg})


@auth_admin
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def add_product(request):
    msg = ''
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']
        image = request.FILES['image']

        new_product = Product(
            product_name = name,
            price = price,
            category = category,
            description = description,
            image = image
        )

        new_product.save()
        msg = 'Succesfully Added'
    return render (request, 'admin_temp/add_product.html',{'msg':msg})

def prod_details(request,pid):
    product = Product.objects.get(id=pid)

    return render(request, 'admin_temp/prod_details.html',{'products':product})

def add_variant(request,pid):
    msg = ''
    if request.method == 'POST':
        quantity = request.POST['quantity']
        size = request.POST['size']
        product_id = Product.objects.get(id=pid)

        new_variant = Variants(
            quantity = quantity,
            size_id = size,
            product_id = product_id
        )

        new_variant.save()
        msg = "Succesfully Added"
    return render(request, 'admin_temp/add_variant.html',{'msg':msg})


def logout(request):
    del request.session['admin']

    request.session.flush()

    return redirect('admin:admin_login')

