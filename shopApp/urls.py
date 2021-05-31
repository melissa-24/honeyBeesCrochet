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
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('theAdmin/categories/', views.addCategory),
    path('theAdmin/createCat/', views.createCat),
    path('theAdmin/categories/<int:category_id>/editCat/', views.editCat),
    path('theAdmin/categories/<int:category_id>/updateCat/', views.updateCat),
    path('theAdmin/categories/<int:category_id>/deleteCat/', views.deleteCat),
    path('theAdmin/topics/', views.addTopic),
    path('theAdmin/createTopic/', views.createTopic),
    path('theAdmin/topics/<int:topic_id>/editTopic/', views.editTopic),
    path('theAdmin/topics/<int:topic_id>/updateTopic/', views.updateTopic),
    path('theAdmin/topics/<int:topic_id>/deleteTopic/', views.deleteTopic),
    path('theAdmin/users/', views.viewUsers),
    path('theAdmin/users/<int:user_id>/editUser/', views.editUser),
    path('theAdmin/users/<int:user_id>/updateUser/', views.updateUser),
    path('theAdmin/users/<int:user_id>/deleteUser/', views.deleteUser),
    path('theAdmin/products/', views.addProduct),
    path('theAdmin/product/createProd/', views.createProd),
    path('theAdmin/product/<int:product_id>/editProd/', views.editProd),
    path('theAdmin/product/<int:product_id>/updateProd/', views.updateProd),
    path('theAdmin/product/<int:product_id>/deleteProd/', views.deleteProd),
    path('dashboard/<int:user_id>/profile/', views.profile),
    path('dashboard/<int:user_id>/editProfile/', views.editProfile),
    path('dashboard/<int:user_id>/updateProfile/', views.updateProfile),
    path('dashboard/<int:user_id>/deleteProfile/', views.deleteProfile),
    path('hangouts/<int:topic_id>/addPost/', views.addPost),
    path('hangouts/post/<int:topic_id>/createPost/', views.createPost),
    path('hangouts/post/<int:post_id>/editPost/', views.editPost),
    path('hangouts/post/<int:post_id>/updatePost/', views.updatePost),
    path('hangouts/post/<int:post_id>/deletePost/', views.deletePost),
    path('hangouts/post/<int:post_id>/addReply/', views.addComment),
    path('hangouts/post/<int:post_id>/createReply/', views.createComment),
    path('hangouts/reply/<int:comment_id>/editReply/', views.editComment),
    path('hangouts/reply/<int:comment_id>/updateReply/', views.updateComment),
    path('hangouts/reply/<int:comment_id>/deleteReply', views.deleteComment),
    path('hangouts/post/<int:post_id>/addLike/', views.addLike),
]