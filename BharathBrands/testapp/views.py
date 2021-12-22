from django.shortcuts import render,redirect
from testapp.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from testapp.models import *
import csv
# Create your views here.
def home(request):
    return render(request,'testapp/index.html')
def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            print('Forms Validated')
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('home')
    return render(request,'registration/signup.html',{'form':form})
def account_views(request):
    form=NewAccountForm
    if request.method=='POST':
        form=NewAccountForm(request.POST)
        if form.is_valid():
            form.save()
        form=NewAccountForm
        acc_detail=NewAccount.objects.all()
        return render(request,'testapp/account.html',{'form':form,'acc_detail':acc_detail})
    acc_detail=NewAccount.objects.all()
    return render(request,'testapp/account.html',{'form':form,'acc_detail':acc_detail})
def account_delete(request,account_number):
    account=NewAccount.objects.get(account_number=account_number)
    print(account)
    account.delete()
    return redirect('/create-account')
def account_edit(request,account_number):
    account=NewAccount.objects.get(account_number=account_number)
    form=NewAccountForm(instance=account)
    if request.method=='POST':
        form=NewAccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
        return redirect('/create-account')
    return render(request,'testapp/edit.html',{'form':form})
def expense_views(request):
    form=NewExpenseForm()
    if request.method=='POST':
        form=NewExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        form=NewExpenseForm()
        new_expense=NewExpense.objects.all()
        return render(request,'testapp/expense.html',{'exp_form':form,'new_expense':new_expense})
    new_expense=NewExpense.objects.all()
    return render(request,'testapp/expense.html',{'exp_form':form,'new_expense':new_expense})
def expense_delete(request,id):
    expense=NewExpense.objects.get(id=id)
    expense.delete()
    return redirect('/create-expense')
def expense_edit(request,id):
    expense=NewExpense.objects.get(id=id)
    form=NewExpenseForm(instance=expense)
    if request.method=='POST':
        form=NewExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/create-expense')
    return render(request,'testapp/expense_edit.html',{'form':form})
def department_views(request):
    form=NewDepartForm()
    if request.method=='POST':
        form=NewDepartForm(request.POST)
        if form.is_valid():
            form.save()
        form=NewDepartForm()
        new_depart=NewDepart.objects.all()
        return render(request,'testapp/department.html',{'form':form,'new_depart':new_depart})
    form=NewDepartForm()
    new_depart=NewDepart.objects.all()
    return render(request,'testapp/department.html',{'form':form,'new_depart':new_depart})
def depart_delete(request,id):
    department=NewDepart.objects.get(id=id)
    department.delete()
    return redirect('/create-depart')
def depart_edit(request,id):
    department=NewDepart.objects.get(id=id)
    form=NewDepartForm(instance=department)
    if request.method=='POST':
        form=NewDepartForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
        return redirect('/create-depart')
    return render(request,'testapp/depart_edit.html',{'form':form})
def item_expense_view(request):
    form=ItemExpenseForm()
    if request.method=='POST':
        form=ItemExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        form=ItemExpenseForm()
        data=ItemExpense.objects.all()
        return render(request,'testapp/item_expense.html',{'form':form,'data':data})
    data=ItemExpense.objects.all()
    return render(request,'testapp/item_expense.html',{'form':form,'data':data})
def item_expense_edit(request,id):
    item_expense=ItemExpense.objects.get(id=id)
    form=ItemExpenseForm(instance=item_expense)
    if request.method=='POST':
        form=ItemExpenseForm(request.POST,instance=item_expense)
        if form.is_valid():
            form.save()
        return redirect('/item-expense')
    return render(request,'testapp/item_expense_edit.html',{'form':form})
def item_expense_delete(request,id):
    item_expense=ItemExpense.objects.get(id=id)
    item_expense.delete()
    return redirect('/item-expense')
def hr_expense_view(request):
    if request.method=='POST':
        form=HrExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        form=HrExpenseForm()
        data=HrExpense.objects.all()
        return render(request,'testapp/hr_expense.html',{'form':form,'data':data})
    form=HrExpenseForm()
    data=HrExpense.objects.all()
    return render(request,'testapp/hr_expense.html',{'form':form,'data':data})
def hr_expense_edit(request,id):
    hr_expense=HrExpense.objects.get(id=id)
    form=HrExpenseForm(instance=hr_expense)
    if request.method=='POST':
        form=HrExpenseForm(request.POST,instance=hr_expense)
        if form.is_valid():
            form.save()
        return redirect('/hr-expense')
    return render(request,'testapp/hr_expense_edit.html',{'form':form})
def hr_expense_delete(request,id):
    hr_expense=HrExpense.objects.get(id=id)
    hr_expense.delete()
    return redirect('/hr-expense')
def misc_expense_view(request):
    if request.method=='POST':
        form=MiscExpensesForm(request.POST)
        if form.is_valid():
            form.save()
        form=MiscExpensesForm()
        data=MiscExpenses.objects.all()
        return render(request,'testapp/misc_expense.html',{'form':form,'data':data})
    form=MiscExpensesForm()
    data=MiscExpenses.objects.all()
    return render(request,'testapp/misc_expense.html',{'form':form,'data':data})
def misc_expense_edit(request,id):
    misc_expense=MiscExpenses.objects.get(id=id)
    form=MiscExpensesForm(instance=misc_expense)
    if request.method=='POST':
        form=MiscExpensesForm(request.POST,instance=misc_expense)
        if form.is_valid():
            form.save()
        return redirect('/misc-expense')
    return render(request,'testapp/misc_expense_edit.html',{'form':form})
def misc_expense_delete(request,id):
    misc_expense=MiscExpenses.objects.get(id=id)
    misc_expense.delete()
    return redirect('/misc-expense')
def generate_report(request):
    if request.method=='POST':
        form=GenerateReportForm(request.POST)
        if form.is_valid():
            form.save()
        response=HttpResponse(content_type='text/csv')
        response['Content-Description']='attachment;filename="reports.csv"'
        report=GenerateReport.objects.all()
        write=csv.writer(response)
        print(report)
        for data in report:
            write.writerow([data.expense_type,data.account_number,data.department_name,data.item_name,data.from_date,data.to_date])
        return response
    form=GenerateReportForm()
    return render(request,'testapp/generate_report.html',{'form':form})
