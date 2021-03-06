from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# ------------------------ Unprotected pages ------------------------

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

def blog(request):
    pass

# ------ Shop Landing Page ------
def shop(request):
    allProds = Product.objects.all()
    if 'user_id' not in request.session:
        context = {
            'allProds': allProds,
        }
        return render(request, 'shop.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'allProds': allProds,
        }
        print(allProds)
        return render(request, 'protected/mainPages/shop.html', context)

# ------ Login Landing Page ------
def login(request):
    return render(request, 'logReg/login.html')

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
    comments = Reply.objects.all()
    posts = Post.objects.all()
    author = Post.objects.all().values()
    replies = Reply.objects.all().values()
    allTopics = Topic.objects.all()
    if 'user_id' not in request.session:
        users = User.objects.all()
        context = {
            'user': users,
            'posts': posts,
            'allTopics': allTopics,
            'author': author,
            'comments': comments,
            'replies': replies,
        }
        return render(request, 'hangouts.html',context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'posts': posts,
            'allTopics': allTopics,
            'author': author,
            'comments': comments,
            'replies': replies,
        }
        return render(request, 'protected/mainPages/hangouts.html', context)

# ------ Hangouts Login Landing Page ------
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
    userInfo = User.objects.all().values()
    if user.acct_id == 1:
        context = {
            'user': user,
        }
        print(userInfo)
        return render(request, 'protected/dashboard.html', context)
    else:
        context = {
            'user': user,
        }
        return render(request, 'protected/adminDashboard.html', context)

# ------------ Protected Admin Pages ------------

# ------ Add Hangouts Topic Landing Page ------
def addTopic(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = User.objects.get(id=request.session['user_id'])
    if user.acct_id == 1:
        messages.error(request, 'Sorry you do not have access to this content')
        return redirect('/')
    context = {
        'topics': Topic.objects.all().values(),
    }
    return render(request, 'protected/admin/topics.html', context)

# ------ Add Topic Route ------
def createTopic(request):
    Topic.objects.create(
        topicName=request.POST['topicName']
    )
    return redirect('/theAdmin/topics')

# ------ Manage Topic Landing ------
def editTopic(request, topic_id):
    oneTopic = Topic.objects.get(id=topic_id)
    context = {
        'editTopic': oneTopic,
    }
    return render(request, 'protected/admin/edit/editTopic.html', context)

# ------ Update Topic Route ------
def updateTopic(request, topic_id):
    toUpdate = Topic.objects.get(id=topic_id)
    toUpdate.topicName = request.POST['topicName']
    toUpdate.save()
    return redirect(f'/theAdmin/topics/{topic_id}/editTopic/')

# ------ Delete Topic Route ------
def deleteTopic(request, topic_id):
    toDelete = Topic.objects.get(id=topic_id)
    toDelete.delete()

    return redirect('/theAdmin/topics/')

# ------ View All Users Landing Page ------
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
        'allUser': allUser,
    }
    return render(request, 'protected/admin/users.html', context)

# ------ Update user Landing Page ------
def editUser(request, user_id):
    oneUser = User.objects.get(id=user_id)
    context = {
        'editUser': oneUser,
        'accts': Acct.objects.all().values(),
    }
    return render(request, 'protected/admin/edit/editUser.html', context)

# ------ Route to update user ------
def updateUser(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.email = request.POST['email']
    toUpdate.username = request.POST['username']
    toUpdate.acct_id = request.POST['acct_id']
    toUpdate.save()
    return redirect(f'/theAdmin/users/{user_id}/editUser/')

# ------ Add Topic Route ------
def deleteUser(request, user_id):
    toDelete = User.objects.get(id=user_id)
    toDelete.delete()

    return redirect('/theAdmin/users/')

# ------ Add Product Landing Page ------
def addProduct(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = User.objects.get(id=request.session['user_id'])
    products = Product.objects.all().values()
    if user.acct_id == 1:
        messages.error(request, 'Sorry you do not have access to this content')
        return redirect('/')
    else:
        context = {
            'user': user,
            'products': products,
        }
        return render(request, 'protected/admin/products.html', context)

# ------ Add Product Route ------
def createProd(request):
    Product.objects.create(
        itemName=request.POST['itemName'],
        itemDescription=request.POST['itemDescription'],
        itemPrice=request.POST['itemPrice'],
        itemImg=request.POST['itemImg'],
    )
    return redirect('/theAdmin/products/')

# ------ View Product Landing Page ------
def editProd(request):
    pass

# ------ Update Product Route ------
def updateProd(request):
    pass

# ------ Delete Product Route ------
def deleteProd(request):
    pass


# ------------ Protected Customer Pages ------------
def profile(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page')
        return redirect('/login/')
    else:
        viewUser = User.objects.get(id=request.session['user_id'])
        context = {
            'viewUser': viewUser,
        }
        return render(request, 'protected/profile.html', context)

def editProfile(request, user_id):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to be logged in to edit.')
        return redirect('/login/')
    editUser = User.objects.get(id=user_id)
    context = {
        'editUser': editUser,
    }
    return render(request, 'protected/editUser.html', context)


def updateProfile(request, user_id):
    toUpdate = User.objects.get(id=user_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.email = request.POST['email']
    toUpdate.username = request.POST['username']
    toUpdate.save()
    return redirect(f'/dashboard/{user_id}/profile/')

def profileImg(request, user_id):
    userProfile = User.objects.get(id=request.session['user_id'])
    userProfile.profile.address1 = request.POST['address1']
    userProfile.profile.address2 = request.POST['address2']
    userProfile.profile.city = request.POST['city']
    userProfile.profile.state = request.POST['state']
    userProfile.profile.zipCode = request.POST['zipCode']
    userProfile.profile.image = request.FILES['image']
    userProfile.save()
    return redirect(f'/dashboard/{user_id}/profile/')

# ------------ Protected Hangout Pages ------------

# ------ Make a Post Landing Page ------ 
def addPost(request, topic_id):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to be logged in to post a message')
        return redirect('/hangouts/login.')
    else:
        user = User.objects.get(id=request.session['user_id'])
        oneTopic = Topic.objects.get(id=topic_id)
        context = {
            'addPost': oneTopic,
            'user': user,
        }
        return render(request, 'protected/hangouts/hangoutPost.html', context)

def createPost(request, topic_id):
    Post.objects.create(
        postTitle=request.POST['postTitle'],
        postContent=request.POST['postContent'],
        poster = User.objects.get(id=request.session['user_id']),
        postTopic= Topic.objects.get(id=topic_id),
    )
    return redirect('/hangouts/')

def editPost(request, post_id):
    onePost = Post.objects.get(id=post_id)
    context = {
        'editPost': onePost,
    }
    return render(request, 'protected/hangouts/editPost.html', context)

def updatePost(request, post_id):
    toUpdate = Post.objects.get(id=post_id)
    toUpdate.postTitle = request.POST['postTitle']
    toUpdate.postContent = request.POST['postContent']
    toUpdate.save()

    return redirect('/hangouts/')

def deletePost(request, post_id):
    toDelete = Post.objects.get(id=post_id)
    toDelete.delete()

    return redirect('/hangouts/')

def addReply(request, post_id):
    if 'user_id' not in request.session:
        messages.error(request, 'You need to be logged in to post a message')
        return redirect('/hangouts/login.')
    else:
        user = User.objects.get(id=request.session['user_id'])
    onePost = Post.objects.get(id=post_id)
    replies = Reply.objects.all()
    context = {
        'addReply': onePost,
        'replies': replies,
        'user': user,
    }
    return render(request, 'protected/hangouts/postReply.html', context)

def createReply(request, post_id):
    Reply.objects.create(
        replyText=request.POST['replyText'],
        author = User.objects.get(id=request.session['user_id']),
        replyPost = Post.objects.get(id=post_id)
    )
    return redirect(f'/hangouts/post/{post_id}/addReply/')

def editReply(request):
    pass

def updateReply(request):
    pass

def deleteReply(request):
    pass

def addLike(request, post_id):
    likePost = Post.objects.get(id= post_id)
    userLike = User.objects.get(id=request.session['user_id'])
    likePost.postLike.add(userLike)
    return redirect('/hangouts/')