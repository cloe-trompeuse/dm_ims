from django.db import models
from django.contrib.auth.models import User
from inventory.models import Stock

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     last_login = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.user.username}-{self.user_type}-{self.address}-{self.last_login}'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.phone}-{self.address}-{self.email}'

# class CustomerOrder(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     date_ordered = models.DateTimeField(auto_now=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return f'{self.customer.first_name}-{self.customer.last_name}-{self.date_ordered}-{self.complete}-{self.transaction_id}'

# class CustomerCart(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Stock, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     date_added = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.customer.first_name}-{self.customer.last_name}-{self.product.name}-{self.quantity}-{self.date_added}'