from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Manager.models import*
from Users.models import*

def admin(request):
    Totellocation=location.objects.all().count()
    totelturf=Eturf.objects.all().count()
    totelbooking=booking.objects.all().count()
    totelmanagerrequest=Register.objects.filter(status=0).count()
    approvedmanagers=Register.objects.filter(status=1).count()
    declinedmanagers=Register.objects.filter(status=2).count()
    totelregusers=Register.objects.all().count()
    totelfeedback=contact.objects.all().count()
    totelapprovedUsers=booking.objects.all().count()
    toteldeclinedUsers=booking.objects.filter(status=2).count()
    return render(request,'admin_index.html',{'Totellocation':Totellocation,'totelturf':totelturf,'totelbooking':totelbooking,'totelmanagerrequest':totelmanagerrequest,'approvedmanagers':approvedmanagers,'declinedmanagers':declinedmanagers,'totelregusers':totelregusers,'totelfeedback':totelfeedback,'totelapprovedUsers':totelapprovedUsers,'toteldeclinedUsers':toteldeclinedUsers})
def addloc(request):
    return render(request,'add_locations.html')
def viewloc(request):
    data=location.objects.all()
    return render(request,'view_locations.html',{'data':data})
def addlocation(request):
    if request.method=='POST':
        locationname=request.POST['locationname']
        locationimage=request.FILES['locationimage']
        data=location(locationname=locationname,locationimage=locationimage)
        data.save()
    return redirect('viewloc')

def edit(request,id):
    data=location.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})
def update(request,id):
    if request .method=='POST':
        locationname=request.POST['locationname']
        locationimage=request.FILES['locationimage']
        manager=request.POST['manager']
        try:
            img_c = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = location.objects.get(id=id).image
        location.objects.filter(id=id).update(locationname=locationname,locationimage=locationimage,manager=manager)
    return redirect('viewloc')
def delete(request,id):
        location.objects.filter(id=id).delete()
        return redirect('viewloc')
def addnew(request):
    data=contact.objects.all()
    return render(request,'contact.html',{'data':data})
def viewcontacts(request):
    data=contact.objects.all()
    return render(request,'view_contact.html',{'data':data})
def turf(request):
    data=Register.objects.filter(status=1)
    data1=location.objects.all()
    return render(request,'add_turf.html',{'data':data,'data1':data1})
def addturf(request):
    if request.method=='POST':
        turfname=request.POST['turfname']
        turfimage=request.FILES['turfimage']
        locationname=request.POST['locationname']
        BookingPackage=request.POST['BookingPackage']
        Facilities=request.POST['Facilities']
        Time=request.POST['Time']
        manager=request.POST['manager']
        data=Eturf(turfname=turfname,manager=manager,turfimage=turfimage,locationname=locationname,BookingPackage=BookingPackage,Facilities=Facilities,Time=Time)
        data.save()
    return redirect('views')
def views(request):
    data=Eturf.objects.all()
    return render(request,'viewturf.html',{'data':data})
def regrequest(request):
    data=Register.objects.filter(status=0)
    return render(request,'request_t1.html',{'data':data})
def regapproved(request,id):
    Register.objects.filter(id=id).update(status=1)
    return redirect('approvedreg')
def regdeclained(request,id):
    Register.objects.filter(id=id).update(status=2)
    return redirect('regrequest')
def declained(request):
    data=Register.objects.filter(status=2)
    return render(request,'decline_t2.html',{'data':data})
def approvedreg(request):
    data=Register.objects.filter(status=1)
    return render(request,'approved_t3.html',{'data':data})
def edits(request,id):
    data=Eturf.objects.filter(id=id)
    data1=Register.objects.filter(status=1)
    data2=location.objects.all()
    return render(request,'edit_turf.html',{'data':data,'data1':data1,'data2':data2})
def updates(request,id):
    if request .method=='POST':
        turfname=request.POST['turfname']
        locationname=request.POST['locationname']
        BookingPackage=request.POST['BookingPackage']
        Facilities=request.POST['Facilities']
        Time=request.POST['Time']
        manager=request.POST['manager']
        try:
            img_c = request.FILES['turfimage']
            fs=FileSystemStorage()
            file=fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Eturf.objects.get(id=id).turfimage
        Eturf.objects.filter(id=id).update(turfname=turfname,turfimage=file,manager=manager,locationname=locationname,BookingPackage=BookingPackage,Facilities=Facilities,Time=Time)
    return redirect('views')

def deletes(request,id):
        Eturf.objects.filter(id=id).delete()
        return redirect('views')
def userreg(request):
    data=Userreg.objects.all()
    return render(request,'userreg.html',{'data':data})
def viewbookusers(request):
    data=booking.objects.all()
    return render(request,'BUt1.html',{'data':data})
def userapproved(request):
    data=booking.objects.all()
    return render(request,'userapproved.html',{'data':data})
def userdeclined(request):
    data=booking.objects.filter(status=2)
    return render(request,'userdeclined.html',{'data':data})
def hey(request):
    return render(request,'hey.html')
