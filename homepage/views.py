from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, CreateView
from inventory.models import Stock
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from transactions.models import SaleBill, PurchaseBill
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"

def stock(request):
    stocks = Stock.objects.filter(is_deleted=False)

    context = {
        'stocks': stocks
    }

    return render(request, 'home.html', context)

# list all users
def UserView(request):
    users = User.objects.all()
        
    context = {
        'users': users,
    }
        
    return render(request, 'user.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users')

    context = {
        'form': form
    }

    return render(request, 'user_create.html', context)

# def register(request):  
#     if request.method == 'POST':  
#         form = CustomUserCreationForm(request.POST)  
        
#         if form.is_valid():  
#             form.save()
#             return redirect('users')
#     else:  
#         form = CustomUserCreationForm()  
    
#     context = {  
#         'form':form  
#     } 

#     return render(request, 'user_create.html', context)  

def user_delete(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('users')
    
    return render(request, 'user_delete.html')