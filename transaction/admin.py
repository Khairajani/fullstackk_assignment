from django.contrib import admin
from django.db import models
from .models import Transaction, TransactionItemDetail, Inventory
import datetime 

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','transaction_number','transaction_status','company','branch',)
    readonly_fields = ('transaction_number',)

    # cnt = 0
    # year = 2021

    

    # def save_model(self, request, instance, form, change):    
    #     curr_year = datetime.datetime.now().year
    #     if curr_year!=self.year:
    #         self.year = curr_year
    #         self.cnt = 1
    #     else:
    #         self.cnt+=1
        
    #     instance.transaction_number = "TRN/"+str(self.cnt)+"/"+str(self.year)
    #     # instance.transaction_number.save()
    #     super().save_model(request, instance, form, change)

@admin.register(TransactionItemDetail)
class TransactionItemDetailAdmin(admin.ModelAdmin):
    list_display = ('id','transaction_id','required_date','qty','rate','unit','article','colour',)

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id','transaction_item_id','gross_qty','net_qty','unit','company','article','colour',)
