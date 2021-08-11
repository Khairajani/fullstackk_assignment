from django.db import models
import datetime
from django.core.validators import MinValueValidator

# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.short_name


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)
    
    def __str__(self):
        return self.name

# Create your models here.

class Transaction(models.Model):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CLOSE = 'CLOSE'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CLOSE, 'Close')]

    company = models.ForeignKey(CompanyLedgerMaster, on_delete = models.CASCADE)
    branch = models.ForeignKey(BranchMaster, on_delete = models.CASCADE)
    department = models.ForeignKey(DepartmentMaster, on_delete = models.CASCADE)
    transaction_number = models.CharField(max_length=50, blank=True, unique=True)
    transaction_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING,)
    remarks = models.CharField(max_length=64, blank=True)
    
    def __str__(self):
        return self.transaction_number

class TransactionItemDetail(models.Model):
    
    KG = 'KG'
    METRE = 'M'
    UNIT_CHOICES = [
        (KG, 'Kg'),
        (METRE, 'Metre'),]

    transaction_id = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete = models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete = models.CASCADE)
    required_date = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    qty = models.FloatField()
    rate = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=KG,)
    
    def __str__(self):
        return str(self.id)

class Inventory(models.Model):
    
    KG = 'KG'
    METRE = 'M'
    UNIT_CHOICES = [
        (KG, 'Kg'),
        (METRE, 'Metre'),]

    transaction_item_id = models.ForeignKey(TransactionItemDetail, on_delete = models.CASCADE)
    article = models.ForeignKey(ArticleMaster, on_delete = models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete = models.CASCADE)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete = models.CASCADE)
    gross_qty = models.FloatField()
    net_qty = models.FloatField()
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=KG,)

    def __str__(self):
        return str(self.id)