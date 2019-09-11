from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import Expense, Income, CustomUser


class CustomUserSerializer(ModelSerializer):
    expenses = serializers.StringRelatedField(many=True, read_only=True)
    incomes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'wallet', 'email', 'expenses', 'incomes']


class ExpenseSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = ['text', 'value', 'date']


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ['text', 'value', 'date']
