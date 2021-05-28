from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('shop/', views.shop),
    path('login/', views.login),
    path('login/access/', views.access),
    path('login/register/', views.register),
    path('login/signup/', views.signup),
    path('hangouts/', views.hangouts),
    path('hangouts/login/', views.hangoutLogin),
    path('hangouts/access/', views.hangoutAccess),
    path('hangouts/register/', views.hangoutRegister),
    path('hangouts/signup/', views.hangoutSignup),
    path('theAdmin/', views.theAdmin),
    path('theAdmin/createAcct/', views.createAcct),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('theAdmin/products/', views.addProduct),
    path('theAdmin/categories/', views.addCategory),
    path('theAdmin/topics/', views.addTopic),
    path('theAdmin/users/', views.viewUsers),
    path('theAdmin/users/<int:user_id>/editUser/', views.editUser),
    path('theAdmin/users/<int:user_id>/updateUser/', views.updateUser),
    path('theAdmin/product/createProduct/', views.createProduct),
    path('theAdmin/product/<int:product_id>/', views.viewAdminProduct),
    path('theAdmin/category/createCategory/', views.createCategory),
    path('theAdmin/topic/createTopic/', views.createTopic),
    path('theAdmin/product/assignCategory/', views.assignCategory),
    path('dashboard/<int:user_id>/profile/', views.profile),
    path('dashboard/<int:user_id>/updateProfile/', views.updateProfile),
    path('dashboard/<int:user_id>/deleteProfile/', views.deleteProfile),
    path('hangouts/addPost/', views.addPost),
    path('hangouts/post/createPost/', views.createPost),
    path('hangouts/post/createComment/', views.createComment),
]