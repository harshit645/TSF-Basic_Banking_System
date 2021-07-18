from os import name
from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('',views.indexPage,name="HomePage"),
    path('customers/',views.customers,name="Customers"),
    path('transfermoney/',views.transfer,name="TransferMoney"),
    path('transactionhistory/',views.history,name="TransactionHistory"),
    path('transfernow/<int:myid>',views.transfernow,name="TransferNow"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
