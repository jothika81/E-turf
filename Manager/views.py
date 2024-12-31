from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Admin.models import*
from Users.models import*

def manager(request): 
    i=request.session.get('username_u')
    Totellocation=location.objects.all().count()
    totelturf=Eturf.objects.all().count()
    totelbooking=booking.objects.filter(status=0).count()
    toteluserrequest=Userreg.objects.filter(status=0).count()
    approveduser=Userreg.objects.filter(status=1).count()
    declineduser=Userreg.objects.filter(status=2).count()
    ownturf=Eturf.objects.filter(manager=i).count()
    return render(request,'manager_index.html',{'Totellocation':Totellocation,'totelturf':totelturf,'totelbooking':totelbooking,'toteluserrequest':toteluserrequest,'approveduser':approveduser,'declineduser':declineduser,'ownturf':ownturf})
def loginM(request): 
    return render(request,'login.html')
def addmanager(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        Phonenum=request.POST['Phonenum']
        Gender=request.POST['Gender']
        data=Register(username=username,password=password,email=email,Phonenum=Phonenum,Gender=Gender)
        data.save()
    return redirect('loginM')
def registerM(request):
    return render(request,'reg.html')
def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(username=username,password=password).exists():
           data = Register.objects.filter(username=username,password=password).values('id','email','Phonenum','Gender').first()
           request.session['m_id'] = data['id']
           request.session['email_u'] = data['email'] 
           request.session['Phonenum_u'] = data['Phonenum']
           request.session['Gender_u'] = data['Gender']  
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('history') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('loginM')
def managerlogout(request):
    del request.session['m_id']
    del request.session['email_u'] 
    del request.session['Phonenum_u'] 
    del request.session['Gender_u']  
    del request.session['username_u']
    del request.session['password_u']
    return redirect('manager')
def Manlocations(request):
    
    data=location.objects.all()
    return render(request,'locations.html',{'data':data})
def history(request):
    s=request.session.get('username_u')
    data= Register.objects.filter(username=s)
    return render(request,'reghistory.html',{'data':data})
def bookeduser(request):
    data=booking.objects.all()
    return render(request,'viewbooking.html',{'data':data})
def BUrequest(request):
    data=booking.objects.filter(status=0)
    return render(request,'BU_request.html',{'data':data})
def BUapproved(request,id):
    booking.objects.filter(id=id).update(status=1)
    return redirect('approvedBU')
def BUdeclained(request,id):
    booking.objects.filter(id=id).update(status=2)
    return redirect('BUrequest')
def declainedBU(request):
    data=booking.objects.filter(status=2)
    return render(request,'BU_decline.html',{'data':data})
def approvedBU(request):
    data=booking.objects.filter(status=1)
    return render(request,'BU_approved.html',{'data':data})
def Allturf(request):
    data=Eturf.objects.all()
    return render(request,'All_turf.html',{'data':data})
def Ownturf(request):
    i=request.session.get('username_u')
    data= Eturf.objects.filter(manager=i)
    return render(request,'Own_turf.html',{'data':data})