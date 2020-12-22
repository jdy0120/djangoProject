from django.shortcuts import render

# Create your views here.

def store(request): #메인
    context = {}
    return render(request, 'store/store.html',context)

def cart(request): # 카트
    context = {}
    return render(request, 'store/cart.html',context)


def checkout(request): # 결제
    context = {}
    return render(request, 'store/checkout.html',context)
