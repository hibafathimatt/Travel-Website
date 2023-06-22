from django.shortcuts import render,redirect
from.models import reg_tb1,tra_tb1,trb_tb1
# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        num=request.POST.get('fn')
        pha=request.POST.get('pn')
        ema=request.POST.get('em')
        pas=request.POST.get('ps')
        de=request.POST.get('to')
        obj=reg_tb1.objects.create(fn=num,pn=pha,em=ema,ps=pas,to=de)
        obj.save()
        if obj:
            return render(request,"login.html")
        else:
            return render(request,"reg.html")
    else:
        return render(request,"reg.html")
def login(request):
    if request.method=='POST':
        em1=request.POST.get('em')
        ps1=request.POST.get('ps')
        obj=reg_tb1.objects.filter(em=em1,ps=ps1)
        if obj:
         request.session['ema']=em1
         request.session['psa']=ps1
         return render(request,"index.html")
        else:
            request.session['ema']=''
            request.session['psa']=''
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def details(request):
    obj=reg_tb1.objects.all()
    return render (request,"details.html",{"data":obj})
def edit(request):
    idno=request.GET.get('idn')
    obj=reg_tb1.objects.filter(id=idno)
    return render(request,"details2.html",{"data":obj})
def update(request):
    if request.method=='POST':
        idn=request.POST.get('idno')
        fnm=request.POST.get('fn')
        pn1=request.POST.get('pn')
        em1=request.POST.get('em')
        ps1=request.POST.get('ps')
        de=request.POST.get('to')
        obj=reg_tb1.objects.get(id=idn)
        obj.fn=fnm
        obj.pn=pn1
        obj.em=em1
        obj.ps=ps1
        obj.to=de
        obj.save()
        return redirect("/details")
    return render(request,"details2.html")
def delete(request):
    idno=request.GET.get('idn')
    obj=reg_tb1.objects.filter(id=idno)
    obj.delete()
    return redirect("/details")
def upload(request):
    if request.method=='POST':
        tde=request.POST.get('te')
        tim=request.FILES.get('ti')
        obj=tra_tb1.objects.create(te=tde,ti=tim)
        obj.save()
        if obj:
            msg="file uploaded"
            return render(request,"traupload.html",{'successful':msg})
        else:
            return render(request,"traupload.html")
    else:
        return render(request,"traupload.html")
def traview(request):
    obj=tra_tb1.objects.all()
    return render(request,"traview.html",{"view":obj})
def destination(request):
    obj=tra_tb1.objects.all()
    return render(request,"destination.html")
def edit(request):
    idno=request.GET.get('idn')
    obj=tra_tb1.objects.filter(id=idno)
    return render(request,"details4.html",{"data":obj})
def update(request):
    if request.method=='POST':
        idn=request.POST.get('idno')
        fnm=request.POST.get('te')
        obj=tra_tb1.objects.get(id=idn)
        obj.te=fnm
        obj.save()
        return redirect("/details3")
    return render(request,"details4.html")
def hampi(request):
    return render(request,"hampi.html")
def home(request):
    return render(request,"home.html")
def book(request):
    return render(request,"book.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def hampii(request):
    return render(request,"hampii.html")
def custom(request):
    return render(request,"custom.html")
