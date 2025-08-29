from django.shortcuts import render,redirect,get_object_or_404
from .models import Library 
from .forms import LibraryForm

# Create your views here.

def book_list(request):
    books=Library.objects.all()
    return render(request,'library/book_list.html',{'books':books}) 

def book_create(request):
    if(request.method=='POST'):
        book=LibraryForm(request.POST)
        print(request.POST)
        if book.is_valid():
            book.save()
            return redirect('booklist')
        else:
            return render(request,'library/book_form.html',{'book':book})

    else:
        book=LibraryForm()
        return render(request,'library/book_form.html',{'book':book})

def book_update(request,id):
    book=get_object_or_404(Library,id=id)
    if(request.method=='POST'):
        book=LibraryForm(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect('booklist')
    else:
        book=LibraryForm(instance=book)
        return render(request,'library/book_form.html',{'book':book}) 
    
def book_delete(request,id):
    book=get_object_or_404(Library,id=id)
    if(request.method=='POST'):
        book.delete()
        return redirect('booklist')
    else:
        return render(request,'library/book_delete_form.html',{'book':book})