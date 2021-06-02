from django.db import models
import re

from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# ---------- User Tables ----------
class Acct(models.Model):
    acctType = models.CharField(max_length=45, default='General')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    acct = models.ForeignKey(Acct, related_name='users', on_delete=CASCADE)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, default='Null')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    owner = models.ForeignKey(User, related_name='profiles', on_delete=CASCADE)
    
# ---------- Hangouts Tables ----------
class Topic(models.Model):
    topicName = models.CharField(max_length=255)

class Post(models.Model):
    postTitle = models.CharField(max_length=255)
    postContent = models.TextField()
    poster = models.ForeignKey(User, related_name='posts', on_delete=CASCADE)
    postTopic = models.ForeignKey(Topic, related_name='topics', on_delete=CASCADE)
    postLike = models.ManyToManyField(User, related_name='likes')
    postCreatedAt = models.DateTimeField(auto_now_add=True)
    postUpdatedAt = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    replyText = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=CASCADE)
    replyPost = models.ForeignKey(Post, related_name='thePost', on_delete=CASCADE)
    replyCreatedAt = models.DateTimeField(auto_now_add=True)
    replyUpdatedAt = models.DateTimeField(auto_now=True)



# ---------- Products Tables ----------
class Category(models.Model):
    catName = models.CharField(max_length=45)

class Product(models.Model):
    itemName = models.CharField(max_length=45)
    itemDescription = models.TextField()
    itemPrice = models.DecimalField(decimal_places=2, max_digits=5)
    itemImg = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name='products')

class Order(models.Model):
    quantity = models.IntegerField()
    totalPrice = models.DecimalField(decimal_places=2, max_digits=7)
    itemsOrdered = models.ManyToManyField(Product, related_name='items')
    shipping = models.ForeignKey(Profile, related_name='address', on_delete=CASCADE)
    customer = models.ForeignKey(User, related_name='orders', on_delete=CASCADE)
