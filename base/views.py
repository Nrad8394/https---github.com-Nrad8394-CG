from django.shortcuts import render

# Create your views here.
def tracking(requests):
        return render(requests,'tracking.html')

def index(requests):
        return render(requests,'index.html')

def order(requests):
        return render(requests,'order.html')

def add_item(requests):
        return render(requests,'add_item.html')
