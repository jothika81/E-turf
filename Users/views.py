from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Admin.models import*
from Manager.models import*
from tkinter import*
import tkinter.messagebox 
def user(request):
    data=location.objects.all()
    data1=Eturf.objects.all()
    return render(request,'index.html',{'data':data,'data1':data1})
def loginuser(request):
    return render(request,'login_user.html')
def status(request):
    root = Tk()
    tkinter.messagebox.showinfo("succesfully registered","successfully registerd" )
    root.mainloop()
def adduser(request):
    if request.method=='POST':
        username=request.POST['Name']
        password=request.POST['password']
        email=request.POST['email']
        Phonenum=request.POST['Phonenum']
        data=Userreg(username=username,password=password,email=email,Phonenum=Phonenum)
        data.save()
        return redirect('status')
def registeruser(request):
    return render(request,'reg_user.html')


def publicdatas(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Userreg.objects.filter(username=username,password=password).exists():
           data = Userreg.objects.filter(username=username,password=password).values('id','email','Phonenum').first()
        
           request.session['u_id'] = data['id']
           request.session['email_u'] = data['email'] 
           request.session['Phonenum_u'] = data['Phonenum'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('user') 
        else:
            return render(request,'login_user.html',{'msg':'invalid user credentials'})
    else:
        return redirect('loginuser')

def userlogouts(request):
    del request.session['u_id']
    del request.session['email_u']
    del request.session['Phonenum_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('user')
def turfdetails(request):
    data=location.objects.all()
    return render(request,'turfdetails.html',{'data':data})
def viewturf(request,locationname):
    if (locationname == 'all'):
        data=Eturf.objects.all()
    else:
        data=Eturf.objects.filter(locationname=locationname)
    return render(request,'view_turf.html',{'data':data})
def about(request):
    return render(request,'about.html')
def addcontacts(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        text=request.POST['text']
        data=contact(Name=Name,Email=Email,text=text)
        data.save()
    return redirect('addnew')
def turfview(request):
    data=Eturf.objects.all()
    return render(request,'view_turf.html',{'data':data})
def turfdetailed(request,id):
    data=Eturf.objects.filter(id=id)
    return render(request,'turfdetails.html',{'data':data})
def alllocations(request):
    data=location.objects.all()
    return render(request,'all_locations.html',{'data':data})
def bookusers(request,id):
    data1=Eturf.objects.filter(id=id)
    return render(request,'booking.html',{'data1':data1})
def bookingid(request,id):
    if request.method=='POST':
        username=request.session.get('u_id')
        Email=request.session.get('email_u')
        Date=request.POST['Date']
        Time=request.POST['Time']
        data=booking(username=Userreg.objects.get(id=username),Email=Email,Date=Date,Time=Time,turfname=Eturf.objects.get(id=id))
        data.save()
    return redirect('bookinghistory')
def bookinghistory(request):
    s=request.session.get('u_id')
    data= booking.objects.filter(username=s)
    return render(request,'bookinghistory.html',{'data':data})
