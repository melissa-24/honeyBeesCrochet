from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# ------------ Unprotected pages ------------

# ------ Main Landing Page ------
def index(request):
    # user = User.objects.get(id=request.session['user_id'])
    # context = {
    #     'user': user,
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')

# ------ About Landing Page ------
def about(request):
    return render(request, 'about.html')

# ------ Contact Landing Page ------
def contact(request):
    return render(request, 'contact.html')

# ------ Shop Landing Page ------
def shop(request):
    return render(request, 'shop.html')

# ------ Login Landing Page ------
def login(request):
    return render(request, 'logreg/login.html')

# ------ Login Route ------
def access(request):
    pass

# ------ Register Landing Page ------
def register(request):
    pass

# ------ Register Route ------
def signup(request):
    pass

# ------ Hangouts Landing Page ------
def hangouts(request):
    return render(request, 'hangouts.html')

# ------ Hangouts Login Landing Page ------
# Same table as regular log in just redirects back to hangouts
def hangoutLogin(request):
    pass

# ------ Hangouts Login Route ------
def hangoutAccess(request):
    pass

# ------ Hangouts Register Page ------
def hangoutRegister(request):
    pass

# ------ Hangouts Register Route ------
def hangoutSignup(request):
    pass


# ------------ Protected Admin Pages ------------

# ------ Add to Store Landing Page ------
def addItems(request):
    pass

def createCategory(request):
    pass

def createOrderType(request):
    pass

def createProduct(request):
    pass

def assignCategory(request):
    pass

# ------------ Protected Customer Pages ------------


# ------------ Protected Hangout Pages ------------

# ------ Make a Post Landing Page ------ 
def addPost(request):
    pass

def createTopic(request):
    pass

def createPost(request):
    pass

def createComment(request):
    pass
