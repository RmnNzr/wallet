from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='name'),
    path('api/expense', views.ExpenseView.as_view(), name='expense'),
    path('api/income', views.IncomeView.as_view(), name='income'),
    path('api/myaccount', views.UserView.as_view(), name='myaccount'),
    path('api/register', views.userRegister, name='register')
]
