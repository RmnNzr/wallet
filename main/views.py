"""filan """
from datetime import datetime, timedelta
# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serialziers import ExpenseSerializer, IncomeSerializer, CustomUserSerializer
from .models import Expense, Income
from .forms import NewForm
# Create your views here.

@csrf_exempt
def userRegister(request):
    form = NewForm(request.POST)
    if form.is_valid():
        current_user = form.save()
        current_token = Token(current_user)
        key = current_token.key
        return JsonResponse({
            'username': request.POST['username'],
            'password': request.POST['password1'],
            'key': key
        })
    return JsonResponse({
        'err': form.errors
    })


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(instance=request.user)
        return Response(serializer.data)


class ExpenseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def change_wallet(self, user, value):
        """asasda"""
        user.wallet -= int(value)
        user.save()

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            self.change_wallet(request.user, request.data['value'])
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        from_date = request.data['from'] if 'from' in request.data \
                                        else datetime.now() - timedelta(days=30)
        to_date = request.data['to'] if 'to' in request.data else datetime.now()
        duration_date = [from_date, to_date]
        expenses = Expense.objects.filter(user=request.user, date__range=duration_date)
        if 'text' in request.data:
            expenses = expenses.filter(text=request.data['text'])
        if 'value' in request.data:
            expenses = expenses.filter(value=request.data['value'])
        serializer = ExpenseSerializer(instance=expenses, many=True)
        return Response(serializer.data)


class IncomeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def change_wallet(self, this_user, value):
        this_user.wallet += int(value)
        this_user.save()

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            self.change_wallet(request.user, request.data['value'])
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        from_date = request.data['from'] if 'from' in request.data else datetime.now() - timedelta(days=30)
        to_date = request.data['to'] if 'to' in request.data else datetime.now()
        duration_date = [from_date, to_date]
        incomes = Income.objects.filter(user=request.user, date__range=duration_date)
        if 'text' in request.data:
            incomes = incomes.filter(text=request.data['text'])
        if 'value' in request.data:
            incomes = incomes.fitler(value=request.data['value'])
        serializer = IncomeSerializer(instance=incomes, many=True)
        return Response(serializer.data)
