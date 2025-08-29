from django.urls import path
from . import views
urlpatterns=[
path('set/',views.home),
path('get/',views.get_session),
path('delete/',views.del_session),
path('update/',views.update),
]