from django.shortcuts import render,redirect,get_object_or_404
from . models import Book
from .forms import BookForm

# Create your views here. 

def book_list(request):
    books=Book.objects.all()
    return render(request,'book/book_list.html',{'books':books}) 

def book_create(request):
    if(request.method=='POST'):
        book=BookForm(request.POST)
        if book.is_valid():
            book.save()
            return redirect('books')
    else:
        book=BookForm()
        return render(request,'book/book_form.html',{'book':book})

def book_update(request,id):
    book=get_object_or_404(Book,id=id)
    if(request.method=='POST'):
        book=BookForm(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect('books')
    else:
        book=BookForm(instance=book)
        return render(request,'book/book_form.html',{'book':book})
    
def book_delete(request,id):
    book=get_object_or_404(Book,id=id)
    if(request.method=='POST'):
        book.delete()
        return redirect('books')

    else:
        return render(request,'book/book_delete_form.html',{'book':book})    
