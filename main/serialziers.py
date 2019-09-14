from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import Expense, Income, CustomUser
from datetime import datetime, timedelta

query_last_month = [(datetime.now() - timedelta(days=30)), datetime.now()]


class CustomUserSerializer(ModelSerializer):
    expenses = serializers.SlugRelatedField(many=True,
                                            slug_field='text',
                                            queryset=Expense.objects.filter(date__range=query_last_month))
    incomes = serializers.SlugRelatedField(many=True,
                                           slug_field='text',
                                           queryset=Income.objects.filter(date__range=query_last_month))

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'wallet',
            'email',
            'expenses',
            'incomes'
        ]


class ExpenseSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = ['text', 'value', 'date']


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ['text', 'value', 'date']
