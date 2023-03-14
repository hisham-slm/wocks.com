from django.shortcuts import render,redirect


def auth_customer(function):
    def wrapper(request,*args,**kwargs):
        if 'customer' in request.session:
            return function(request,*args,**kwargs)
        else:
            return redirect('customer:login')
    
    return wrapper