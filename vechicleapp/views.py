from django.shortcuts import render,redirect
from .models import Vechicle
from .form import VechicleForm

# Create your views here.
def index(request):
    vechicle=Vechicle.objects.all()
    context={
        'vechicle_list':vechicle
    }
    return render(request,'index.html',context)

def detail(request,vechicle_id):
    vechicle=Vechicle.objects.get(id=vechicle_id)
    return render(request,'detail.html',{'vechicle':vechicle})

def add_vechicle(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        vechicle=Vechicle(name=name,desc=desc,img=img)
        vechicle.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    vechicle=Vechicle.objects.get(id=id)
    form=VechicleForm(request.POST or None,request.FILES,instance=vechicle)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'vechicle':vechicle})
def delete(request,id):
    if request.method=='POST':
        vechicle=Vechicle.objects.get(id=id)
        vechicle.delete()
        return redirect('/')
    return render(request,'delete.html')


