from django.shortcuts import render,redirect


def auth_admin(function):
    def wrapper(request,*args,**kwargs):
        if 'admin' in request.session:
            return function(request,*args,**kwargs)
        else:
            return redirect('admin:admin_login')
    
    return wrapper