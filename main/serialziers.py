from rest_framework.serializers import Serializer, ModelSerializer


class ExpenseSerialzier(ModelSerializer):
    class Meta:
        model = 