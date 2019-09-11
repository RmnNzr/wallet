from django.shortcuts import render
from rest_framework.views import APIView
from .serialziers import ExpenseSerializer, IncomeSerializer, CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Expense, Income
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(instance=request.user)
        return Response(serializer.data)


class ExpenseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user)
        if 'text' in request.data:
            expenses = expenses.filter(text=request.data['text'])
        serializer = ExpenseSerializer(instance=expenses, many=True)
        return Response(serializer.data)


class IncomeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error,
                        status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        incomes = Income.objects.filter(user=request.user)
        if 'text' in request.data:
            incomes = incomes.filter(text=request.data['text'])
        serializer = IncomeSerializer(instance=incomes, many=True)
        return Response(serializer.data)
