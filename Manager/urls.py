from django.urls import path
from .import views

urlpatterns = [
    path('manager',views.manager,name='manager'),
    path('addmanager',views.addmanager,name='addmanager'),
    path('registerM',views.registerM,name='registerM'),
    path('publicdata',views.publicdata,name='publicdata'),
    path('managerlogout',views.managerlogout,name='managerlogout'),  
    path('loginM',views.loginM,name='loginM'),
    path('Manlocations',views.Manlocations,name='Manlocations'),
    path('bookeduser',views.bookeduser,name='bookeduser'), 
    path('BUrequest',views.BUrequest,name='BUrequest'),
    path('BUapproved/<int:id>',views.BUapproved,name='BUapproved'),
    path('approvedBU',views.approvedBU,name='approvedBU'),
    path('declainedBU',views.declainedBU,name='declainedBU'),
    path('BUdeclained/<int:id>',views.BUdeclained,name='BUdeclained'),
    path('history',views.history,name='history'),
    path('Allturf',views.Allturf,name='Allturf'),
    path('Ownturf',views.Ownturf,name='Ownturf'),
]