from django.db import models

# Create your models here.
class NewAccount(models.Model):
    ACCOUNT_TYPE = (
    ('LOAN','Loan'),
    ('SAVING-BANK', 'Saving-Bank'),
    ('CURRENT-BANK','Current-Bank'),
    ('PETTY CASH','Petty Cash'),
    ('MOBILE WALLET','Mobile Wallet'),
    ('UPI WALLET','UPI Wallet'),
)
    account_number=models.BigIntegerField(primary_key=True)
    account_name=models.CharField(max_length=255)
    description=models.TextField()
    account_type=models.CharField(max_length=255,choices=ACCOUNT_TYPE,default='')
    opening_balance=models.FloatField()
    current_balance=models.FloatField()
    def __str__(self):
        return str(self.account_number)
class NewExpense(models.Model):
    expense_type_name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return str(self.expense_type_name)
class NewDepart(models.Model):
    department_name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.department_name
class Expense(models.Model):
    transaction_id=models.CharField(max_length=255)
    date=models.DateField()
    expense_type=models.OneToOneField(NewExpense,on_delete=models.CASCADE)
    amount=models.FloatField()
    paid_from_account=models.OneToOneField(NewAccount,on_delete=models.CASCADE)
    class Meta:
        abstract=True
class ItemExpense(Expense):
    item_name=models.CharField(max_length=255)
    quantity=models.IntegerField()
    def __str__(self):
        return self.item_name
class HrExpense(Expense):
    staff_name=models.CharField(max_length=255)
    purpose=models.CharField(max_length=255)
    def __str__(self):
        return self.purpose
class MiscExpenses(Expense):
    purpose=models.OneToOneField(HrExpense,on_delete=models.CASCADE)
class GenerateReport(models.Model):
    expense_type=models.OneToOneField(NewExpense,on_delete=models.CASCADE)
    account_number=models.OneToOneField(NewAccount,on_delete=models.CASCADE)
    department_name=models.OneToOneField(NewDepart,on_delete=models.CASCADE)
    item_name=models.OneToOneField(ItemExpense,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField()
