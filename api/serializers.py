from rest_framework import serializers
from .models import *


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        exclude = ['id', 'block']


class BlocksDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)
    class Meta:
        model= Block
        fields = ('block_id', 'timestamp', 'transactions')