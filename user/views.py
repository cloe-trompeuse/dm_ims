from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from .forms import CreateCustomer
from .forms import CreateSiteCustomer
from .models import Customer

# Create your views here.
login_required = 'login'
def customers(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }

    return render(request, 'customers.html', context)

def create_customer(request):
    if request.method == 'POST':
        cust_form = CreateSiteCustomer(request.POST)

        if cust_form.is_valid():
            cust_form.save()
            return redirect('customers')
    else:
        cust_form = CreateSiteCustomer()

    context = {
        'cust_form': cust_form
        }
    return render(request, 'create_customer.html', context)

# def register_customer(request):
#     if request.method == 'POST':
#         form = CreateCustomer(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('customers')
#     else:
#         form = CreateCustomer()

#     context = {
#         'form': form
#         }
#     return render(request, 'create_customer.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customers')

    context = {
        'customer': customer
    }

    return render(request, 'delete_customer.html', context)