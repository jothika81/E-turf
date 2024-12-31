from django.urls import path
from .import views

urlpatterns = [
    path('adminapp',views.admin,name='admin'),
    path('addloc',views.addloc,name='addloc'),
    path('viewloc',views.viewloc,name='viewloc'),
    path('addlocation',views.addlocation,name='addlocation'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update<int:id>',views.update,name='update'),
    path('delete<int:id>',views.delete,name='delete'),
 path('addnew',views.addnew,name='addnew'),
    path('viewcontacts',views.viewcontacts,name='viewcontacts'),
  path('turf',views.turf,name='turf'),
    path('addturf',views.addturf,name='addturf'),
    path('views',views.views,name='views'),
    path('regrequest',views.regrequest,name='regrequest'),
    path('regapproved/<int:id>',views.regapproved,name='regapproved'),
    path('approvedreg',views.approvedreg,name='approvedreg'),
    path('regdeclained/<int:id>',views.regdeclained,name='regdeclained'),
    path('declained',views.declained,name='declained'),
  
    path('edits/<int:id>',views.edits,name='edits'),
    path('updates<int:id>',views.updates,name='updates'),
    path('deletes<int:id>',views.deletes,name='deletes'),
    path('userreg',views.userreg,name='userreg'),
    path('viewbookusers',views.viewbookusers,name='viewbookusers'),
    path('userapproved',views.userapproved,name='userapproved'),
    path('userdeclined',views.userdeclined,name='userdeclined'),
]