from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('trn/', views.addtransaction.as_view(), name="addtransaction"),
    path('trnitem/', views.addtransactionitem.as_view(), name="addtransactionitem"),
    path('invent/', views.addinventory.as_view(), name="addinventory"),
    path('trnview/', views.gettransaction.as_view(), name="gettransaction"),
    path('trndel/', views.deletetransaction.as_view(), name="deletetransaction"),
]
