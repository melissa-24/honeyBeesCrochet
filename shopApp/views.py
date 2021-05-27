from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# ------------ Unprotected pages ------------

# ------ Main Landing Page ------
def index(request):
    if 'user_id' not in request.session:
        return render(request, 'index.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'protected/mainPages/index.html')

# ------ About Landing Page ------
def about(request):
    if 'user_id' not in request.session:
        return render(request, 'about.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'protected/mainPages/about.html', context)

# ------ Contact Landing Page ------
def contact(request):
    if 'user_id' not in request.session:
        return render(request, 'contact.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'protected/mainPages/contact.html', context)

# ------ Shop Landing Page ------
def shop(request):
    if 'user_id' not in request.session:
        return render(request, 'shop.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'protected/mainPages/shop.html')

# ------ Login Landing Page ------
def login(request):
    return render(request, 'logreg/login.html')

# ------ Login Route ------
def access(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/login/register/')

# ------ Register Landing Page ------
def register(request):
    context = {
        'accts': Acct.objects.all()
    }
    return render(request, 'logReg/register.html', context)

# ------ Register Route ------
def signup(request):
    if request.method == 'GET':
        return redirect('/login/register/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/login/register/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw,
        acct_id=request.POST['acct']
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

# ------ Hangouts Landing Page ------
def hangouts(request):
    if 'user_id' not in request.session:
        return render(request, 'hangouts.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
        }
        return render(request, 'protected/mainPages/hangouts.html', context)

# ------ Hangouts Login Landing Page ------
# Same table as regular log in just redirects back to hangouts
def hangoutLogin(request):
    return render(request, 'logReg/hangoutsLogin.html')

# ------ Hangouts Login Route ------
def hangoutAccess(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/hangouts/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/hangouts/register/')

# ------ Hangouts Register Page ------
def hangoutRegister(request):
    return render(request, 'logReg/hangoutsRegister.html')

# ------ Hangouts Register Route ------
def hangoutSignup(request):
    if request.method == 'GET':
        return redirect('/hangouts/register/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/hangouts/register/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw,
        acct_id=request.POST['acct']
    )
    request.session['user_id'] = newUser.id
    return redirect('/hangouts/')

# ------ Accounts Landing Page ------
def theAdmin(request):
    context = {
        'accts': Acct.objects.all().values()
    }
    return render(request, 'theAdmin.html', context)

# ------ Create Acct Route ------
def createAcct(request):
    Acct.objects.create(
        acctType=request.POST['acctType'],
    )
    return redirect('/theAdmin/')

# ------ User Logout ------
def logout(request):
    request.session.clear()
    return redirect('/')

# ------------------------ Protected Pages ------------------------

# ------ Dashboard Post Landing Page ------
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = User.objects.get(id=request.session['user_id'])
    if user.acct_id == 1:
        context = {
            'user': user,
        }
        return render(request, 'protected/dashboard.html', context)
    else:
        context = {
            'user': user,
        }
        return render(request, 'protected/adminDashboard.html', context)

# ------------ Protected Admin Pages ------------

# ------ Add to Store Landing Page ------
def addProduct(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = User.objects.get(id=request.session['user_id'])
    if user.acct_id == 1:
        messages.error(request, 'Sorry you do not have access to this content')
        return redirect('/')
    else:
        context = {
            'user': user,
        }
        return render(request, 'protected/admin/products.html', context)

def addCategory(request):
    
    return render(request, 'protected/admin/categories.html')

def addTopic(request):
    return render(request, 'protected/admin/topics.html')

def viewUsers(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = User.objects.get(id=request.session['user_id'])
    if user.acct_id == 1:
        messages.error(request, 'Sorry you do not have access to this content')
        return redirect('/')
    allUsers = User.objects.all().values()
    allUser = User.objects.all()
    acct = Acct.objects.all().values()
    context = {
        'user': user,
        'allUsers': allUsers,
        'acct': acct,
    }
    print(allUser.username)
    return render(request, 'protected/admin/users.html', context)

def createProduct(request):
    pass

def viewAdminProduct(request):
    pass

def createCategory(request):
    pass

def createTopic(request):
    pass

def assignCategory(request):
    pass

# ------------ Protected Customer Pages ------------
def profile(request):
    pass

def updateProfile(request):
    pass

def deleteProfile(request):
    pass


# ------------ Protected Hangout Pages ------------

# ------ Make a Post Landing Page ------ 
def addPost(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to be logged in to post a message')
        return redirect('/hangouts/login.')

def createPost(request):
    Post.objects.create(
        postTitle=request.POST['postTitle'],
        postContent=request.POST['postContent'],
        postAuthor=request.POST['postAuthor'],
        postTopic=request.POST['postTopic'],
    )

def viewPost(request):
    pass

def updatePost(request):
    pass

def deletePost(request):
    pass

def createComment(request):
    pass

def viewComment(request):
    pass

def updateComment(request):
    pass

def deleteComment(request):
    pass