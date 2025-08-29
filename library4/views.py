from django.shortcuts import render,redirect,get_object_or_404
from .models import Book  
from .forms import BookForm 
from django.contrib import messages

# Create your views here. 

def booklist(request):
    books=Book.objects.all() 
    return render(request,'library4/book_list.html',{'books':books}) 

def book_create(request):
    if(request.method=='POST'): 
        book=BookForm(request.POST) 
        if book.is_valid():
            title=book.cleaned_data['title']
            if Book.objects.filter(title__iexact=title).exists():
                messages.error(request,f'the book with {title} already exists') 
            else:
                book.save()
                return redirect('books')
    else:
        book=BookForm() 
    return render(request,'library4/book_form.html',{'book':book}) 
    
def book_update(request,id):
    book=get_object_or_404(Book,id=id) 
    if request.method=='POST':
        book=BookForm(request.POST,instance=book) 
        if book.is_valid():
            book.save()
            return redirect('books')
    else:
        book=BookForm(instance=book) 
        return render(request,'library4/book_form.html',{'book':book})





