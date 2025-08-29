from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home(request):
    request.session['name']={'name1':'kalyan','name2':'Ravi'}
    request.session['BrotherName']='Rajesh'
    
    

    return HttpResponse("<h3>session key set successfully</h3>") 
# def get(request):
#     name=request.session['name']
#     print(name)
#     return HttpResponse("<h1>Hello World hi</h1>") 
# def get(request):
#     name = request.session.get('name')  # Returns None if key doesn't exist
#     if name is None:
#         return HttpResponse("Name not found in session")
#     print(name)
#     return HttpResponse(f"<h1>Hello {name}</h1>") 
def get_session(request):
    # Safely get 'name' from session (with default if not exists)
    name = request.session.get('name', 'Guest')  # Defaults to 'Guest' if not set 
    # request.session['BrotherName']='Ricky'
    # Bro=request.session.get('BrotherName')
    name=request.session.get('name')
    return HttpResponse(f"<h1>Hello  {name}</h1>") 
def del_session(request):
    request.session.flush()
    return HttpResponse('<h1> complete session  deleted successfully </h1>') 

def update(request):
    request.session['name']['name1']='John'
    request.session.modified=True
    return HttpResponse('update page')