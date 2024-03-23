from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('facility/', views.facility, name='facility'),
    path('ativities/', views.ativities, name='ativities'),
    path('calltoaction/', views.calltoaction, name='calltoaction'),
    # path('my', views.index, name='index')
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('homapage/', views.homapage, name='homapage'),
    path('display_tables/', views.display_tables, name='display_tables'),

    path('submitLoginDetails', views.submitLoginDetails, name='submitLoginDetails'),


    path('addPost/', views.addPost, name='addPost'),
    path('addActivity/', views.addActivity, name='addActivity'),

    path('submit_activity/', views.submit_activity, name='submit_activity'),

    path('posts/', views.posts, name='posts'),
    path('delete_activity/<int:id>/',
         views.delete_activity, name='delete_activity'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),

    path('send_email/', views.send_email, name='send_email'),

]
