from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from .models import Item,Transporter,CustomUser,Order

# Create your views here.
def tracker(request):
        # will display all orders and their status
        order = Order.objects.all()
        context = {
                'order': order
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
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                address = request.POST.get('address')
                phone_number = request.POST.get('phone_number')
                

        try:
                transporter = Transporter.objects.all()
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.transporter.phone_number = phone_number
                user.transporter.address = address
                user.save()
            
                messages.success(request, "Transporter Added Successfully!")
                return redirect('add_transporter')
        except Exception as e:
            print(e)
            messages.error(request, "Failed to Add transporter!")
            return redirect('add_transporter')
    
def add_order(request):     
        return render(request,'base/add_order.html')
def add_order_save(request):
        transporters = Transporter.objects.all()
        items = Item.objects.all()
        context = {
                'transporters': transporters,
                'items': items,
        }
        if request.method != 'POST':
                messages.error(request, 'Invalid Method')
                return redirect('')
        else:
                item_name = request.POST.get('item_name')
                destination = request.POST.get('destination')
                transporter = request.POST.get('transporter')
                receiver_first_name = request.POST.get('receiver_first_name')
                receiver_last_name = request.POST.get('receiver_last_name')
                receiver_id_number = request.POST.get('receiver_id_number')
                receiver_confirmation = request.POST.get('receiver_confirmation')
        try:
                add_order = Order(item_name=item_name,destination=destination,transporter=transporter,
                                  receiver_first_name=receiver_first_name,receiver_last_name=receiver_last_name
                                  ,receiver_id_number=receiver_id_number,receiver_confirmation=receiver_confirmation)
                add_item.save()
                messages.success(request, "Item Added.")
                return redirect('')
        except:
                messages.error(request, "Failed to Add Item.")
                return redirect('')

         
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

