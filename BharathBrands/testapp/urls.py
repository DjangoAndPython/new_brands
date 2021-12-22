from django.urls import path,include
from testapp import views
urlpatterns=[
    path('',views.home),
    path('home',views.home,name='home'),
    path('signup',views.signup),
    path('create-account',views.account_views),
    path('create-expense',views.expense_views),
    path('delete/<account_number>',views.account_delete),
    path('edit/<account_number>',views.account_edit),
    path('delete-expense/<int:id>',views.expense_delete),
    path('edit-expense/<int:id>',views.expense_edit),
    path('create-depart',views.department_views),
    path('delete-depart/<int:id>',views.depart_delete),
    path('edit-depart/<int:id>',views.depart_edit),
    path('item-expense',views.item_expense_view),
    path('item-expense-edit/<int:id>',views.item_expense_edit),
    path('item-expense-delete/<int:id>',views.item_expense_delete),
    path('hr-expense',views.hr_expense_view),
    path('misc-expense',views.misc_expense_view),
    path('hr-expense-edit/<int:id>',views.hr_expense_edit),
    path('hr-expense-delete/<int:id>',views.hr_expense_delete),
    path('misc-expense',views.misc_expense_view),
    path('misc-expense-edit/<int:id>',views.misc_expense_edit),
    path('misc-expense-delete/<int:id>',views.misc_expense_delete),
    path('generate-report',views.generate_report),
    path('accounts/',include('django.contrib.auth.urls'))
]
