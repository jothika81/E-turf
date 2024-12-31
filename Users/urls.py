from django.urls import path
from .import views

urlpatterns = [
    path('',views.user,name='user'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('adduser',views.adduser,name='adduser'),
    path('registeruser',views.registeruser,name='registeruser'),
    path('publicdatas',views.publicdatas,name='publicdatas'),  
    path('userlogouts',views.userlogouts,name='userlogouts'),
     path('turfdetails',views.turfdetails,name='turfdetails'),
    path('viewturf/<str:locationname>',views.viewturf,name='viewturf'),
    path('aboutus',views.about,name='about'),
     path('addcontacts',views.addcontacts,name='addcontacts'), 
      path('turfview',views.turfview,name='turfview'),
    path('turfdetailed/<int:id>',views.turfdetailed,name='turfdetailed'),
    path('alllocations',views.alllocations,name='alllocations'),
    path('bookusers/<int:id> ',views.bookusers,name='bookusers'),
    path('bookingid/<int:id>',views.bookingid,name='bookingid'),
    path('bookinghistory',views.bookinghistory,name='bookinghistory'),
    path('status',views.status,name='status'),
  
]