from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse # > it's for adding the item in cart
import json
import datetime  # -> it's for payment transaction time and date , (this syntax is located in line :94)

from .models import Product, Order
#================
from .models import *
from .models import Customer
#  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# ---------conatct
from django.core.mail import send_mail
# from django.core.mail import BadHeaderError

# --------------------------

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         data = {
#             'name': name,
#             'email':email,
#             'phone':phone,
#             'subject':subject,
#             'message': message,
#         }
#         message = '''
#         New message: {}

#         From: {}
#         '''.format(data['message'], data[email])
#         send_mail(data[subject], message, '', ['ashokgowd34@gmail.com'])

#     return render(request, 'store/contact.html')


from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
        }
        email_message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])

        try:
            
            send_mail(
                data['subject'],
                email_message,
                data['email'],
                ['ashokgowd34@gmail.com']
            )
            print(data['subject'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            logger.error([f'Error sending email: {e}'])
            #return HttpResponse([f'An error occurred: {e}'])

    return render(request, 'store/contact.html')







def authenticate_customer(username, password):
    try:
        customer = Customer.objects.get(name=username)
        if customer.user.check_password(password):  # Assuming password is stored in the User model linked to Customer
            return customer
    except Customer.DoesNotExist:
        return None


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        customer = authenticate_customer(username, pass1)
        if customer is not None:
            login(request,customer.user)
            return redirect('store')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'store/login.html')

def SignupPage(request):
    if request.method=='POST':
        username =request.POST.get('username')
        email =request.POST.get('email')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')
        print(username,email)

        if password1!=password2:
            return HttpResponse("Passwords is not match")
        my_user=User.objects.create_user(username,email,password1)
        
        my_user.save()
        
        customer = Customer(user=my_user, name=username, email=email)
        customer.save()

        return  redirect('login')

        # print(username,email,password1,password2)

    return render(request, 'store/signup.html')

  
def about(request):
    return render(request, 'store/about.html')


# def  acounts(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Authenticate the user
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')  # assuming you use password1 for password field
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 store(request, user)
#                 return redirect('success')  # Ensure 'login' is the correct name of your login URL
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'store/Acounts.html', {'form': form})

# def success(request):
#     return render(request, 'store/store.html')
 
 

def product(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'store/product.html', context)
 


# def store(request):

#       # step-2 
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = [] 
#         order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}  #-> 'shipping':False ==> after creting the shipping model
#         cartItems = order['get_cart_items']

#     # step-1
#     products = Product.objects.all()
#     context = {'products':products, 'cartItems':cartItems }
#     return render(request, 'store/store.html', context)

def store(request):

      # step-2 
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = [] 
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}  #-> 'shipping':False ==> after creting the shipping model
        cartItems = order['get_cart_items']

    # step-1
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems }
    return render(request, 'store/store.html', context)

def cart(request):
    # step-2
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items # =>this from store. for adding the cart-icon
    else:
        items = []   
        # down of syntax is If your not add any item are if server issu from backend then it will display
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}  #-> 'shipping':False ==> after creting the shipping model
        cartItems = order['get_cart_items'] # =>this from store. for adding the cart-icon

    # step-1
    context = {'items':items, 'order':order, 'cartItems':cartItems} #<= 'order':order -> after creating the model.py order, @prorerty 
    return render(request, 'store/cart.html', context)



def checkout(request):
     # step-2
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items # =>this from store. for adding the cart-icon
    else:
        items = []   
        # down of syntax is If your not add any item are if server issu from backend then it will display
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False} #-> 'shipping':False ==> after creting the shipping model
        cartItems = order['get_cart_items'] # =>this from store. for adding the cart-icon

    # step-1
    context = {'items':items, 'order':order, 'cartItems':cartItems } #<= 'order':order -> after creating the model.py order, @prorerty 
    return render(request, 'store/checkout.html', context)

# ------

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
                 

    return JsonResponse('Item was added', safe=False)

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt

# for  payment completion 
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
 
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )    

    else:
        print('User is not Login...')
        

    return JsonResponse('Payment Completed!', safe=False)




# ================================================================


 