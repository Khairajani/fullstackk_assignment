from rest_framework import serializers
from .models import Transaction, TransactionItemDetail, Inventory
import datetime

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
        # fields = ['company','branch','department','remarks']
        # read_only_fields = ['transaction_number','transaction_status']

class TransactionItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionItemDetail
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
