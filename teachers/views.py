from django.shortcuts import render 
from .forms import TeachersForm 
from django.http import HttpResponseRedirect,HttpResponse
from .models import Teacher

# Create your views here. 

def home(request):
    print('virat kholi is king')
    if(request.method=='POST'):
        print(request.POST)
        form=TeachersForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # phone_number=form.cleaned_data['phone_number']
            # bio=form.cleaned_data['bio']
            # teacher=Teacher.objects.create(name=name,email=email,phone_number=phone_number,bio=bio)
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['Bio'])
            form.save()
            return HttpResponseRedirect('/teachers/thank-you')
    else:
        form=TeachersForm()
        return render(request,'teachers/home.html',{'form':form}) 
def thank(request):
    return HttpResponse('<h2>form submitted</h2>') 

def data(request):
    alldata=Teacher.objects.all()
    return render(request,'teachers/all-data.html',{'alldata':alldata}) 

def update(request,id):
    teacher=Teacher.objects.get(id=id)
    if(request.method == 'POST'):
        form=TeachersForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/all-data/')
    else:
        form=TeachersForm(instance=teacher)
    return render(request,'teachers/update.html',{'form':form})

def delete(request,id):
    if request.method=='POST':
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
    return HttpResponseRedirect('/teachers/home/')