from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.views.decorators.csrf import csrf_exempt

from .models import Item,Transporter,CustomUser,Order
from base.EmailBackEnd import EmailBackEnd

from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def loginPage(request):
       return render(request,'login.html')
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            return redirect('tracker')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')
def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" Username: "+request.user.username)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('base/add_order.html')  
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def base(request):
        return render(request, 'base.html')



def tracker(request):
        # will display all orders and their status
        orders = Order.objects.all()
        
        
        context = {
                'orders': orders
        } 
        
        
        return render(request,'base/tracking.html',context) 
def add_item(request):
        return render(request,'base/add_item.html') 

def add_item_save(request):
        if request.method != 'POST':
                messages.error(request, 'Invalid Method')
                return redirect('add_item')
        else:
                item_name = request.POST.get('item_name')
                specification = request.POST.get('specification')
                item_id = request.POST.get('item_id')
        try:
                add_item = Item(item_name=item_name,specification=specification,item_id=item_id)
                add_item.save()
                messages.success(request, "Item Added.")
                return redirect('add_item')
        except Exception as e:
                print(e)
                messages.error(request, "Failed to Add Item.")
                return redirect('add_item')
def add_transporter(request):
        return render(request,'base/add_transporter.html')        
def add_transporter_save(request):
        if request.method != "POST":
                messages.error(request, "Invalid Method ")
                return redirect('add_transporter')
        else:
                transporter_first_name = request.POST.get('first_name')
                transporter_last_name = request.POST.get('last_name')
                transporter_email_address = request.POST.get('email')
                transporter_address = request.POST.get('address')
                transporter_phone_number = request.POST.get('phone_number')
                

        try:
                add_transporter = Transporter(transporter_first_name=transporter_first_name, transporter_last_name=transporter_last_name, transporter_email_address=transporter_email_address,transporter_address=transporter_address,transporter_phone_number = transporter_phone_number)
                add_transporter.save()
            
                messages.success(request, "Transporter Added Successfully!")
                return redirect('add_transporter')
        except Exception as e:
            print(e)
            messages.error(request, "Failed to Add transporter!")
            return redirect('add_transporter')
    
def new_entry(request): 
        transporters = Transporter.objects.all()

        items = Item.objects.all()
        context = {
                'transporters': transporters,
                'items': items,
        }    
        return render(request,'base/new_entry.html',context)

def new_entry_save(request):
        transporters = Transporter.objects.all()
        items = Item.objects.all()
        context = {
                'transporters': transporters,
                'items': items,
        }
        if request.method != 'POST':
                messages.error(request, 'Invalid Method')
                return redirect('new_entry')
        else:
                item_id= request.POST.get('item_name')
                item = Item.objects.get(id=item_id)

                destination = request.POST.get('destination')
                
                item_status = request.POST.get('item_status')
                receiver_first_name = request.POST.get('receiver_first_name')
                receiver_last_name = request.POST.get('receiver_last_name')
                receiver_phone_number = request.POST.get('receiver_phone_number')
                receiver_confirmation = request.POST.get('receiver_confirmation')
        try:
                new_entry = Order(item_id=item,destination=destination,item_status=item_status,
                                  receiver_first_name=receiver_first_name,receiver_last_name=receiver_last_name
                                  ,receiver_phone_number=receiver_phone_number,receiver_confirmation=receiver_confirmation)
                
                new_entry.save()
                messages.success(request, "Order Added.")
                return redirect('new_entry')
        except Exception as e:
                print(e)
                messages.error(request, "Failed to Add Order.")
                return redirect('new_entry')


def print_order(request, unique_code):
    order = get_object_or_404(Order, unique_code=unique_code)
    return render(request, 'print_order.html', {'order': order})  
     
@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

