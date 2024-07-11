from django.db import models
from django.contrib.auth.models import User



# ==> customer table

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return  self.name
    
# ==> Product table

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
              url = self.image.url
        except:
             url = ''
        return url    
      
 
 
# ==> Order-1 table    
class Order(models.Model):
    # step-1
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    # step-3 
    @property
    def shipping(self):
         shipping = False
         orderitems = self.orderitem_set.all()
         for i in orderitems:
              if i.product.digital == False:
                   shipping = True
         return shipping          
    
    # step-2
    @property
    def get_cart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total
    
    # step-3
    @property
    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total

# ==> OrderItem-2 table


class OrderItem(models.Model):
    # step-1
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
   # step-2
    @property
    def get_total(self):
         totle = self.product.price * self.quantity
         return totle

class ShippingAddress(models.Model):
               customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
               order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
               address = models.CharField(max_length=200, null=True)
               city = models.CharField(max_length=200, null=True)
               state = models.CharField(max_length=200, null=True)
               zipcode = models.CharField(max_length=200, null=True)
               data_added = models.DateTimeField(auto_now_add=True)

               def __str__(self):
                    return self.address

 


    # ============================
 

class UserProfile(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # password2 = models.CharField(max_length=128) 

    def __str__(self):
        return self.email
    
    

# from django.contrib.auth.models import User
# from django.db import models

 