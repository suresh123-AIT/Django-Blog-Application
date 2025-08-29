# from django.http import HttpResponse
# def customFunctionMiddleWare(get_response):
#     #one time configuration 
#     print('one time conf')

#     def middleware(request):
#         #code excuted before the view is called-request 
#         print('code excuted before the view')

#         response=HttpResponse('This is Function based middleware')
#         #code excuted after the view -response 
#         print('code excuted after the view')

#         return response 
#     return middleware 


# class customClassMiddleWare:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     #one time configuration 
#     print('one time conf')

#     def __call__(self,request):
#         #code excuted before the view is called-request 
#         print('code excuted before the view') 
#         print(request.path)
#         if(request.path=='/teachers/thank-you/'):
#             print('thank view is called')

#         response= HttpResponse('This is class based middleware')
#         #code excuted after the view -response 
#         print('code excuted after the view')

#         return response
    