from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='auth_token.key', read_only=True)
    class Meta:
        model = User
        fields = ['token', 'username', 'email', 'first_name', 'last_name', 'password']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        Token.objects.get_or_create(user=user)
        
        return user

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        exclude = ['id', 'block']


class BlocksDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)
    class Meta:
        model= Block
        fields = ('block_id', 'timestamp', 'transactions')
        
        
class TransactionsDetailSerializer(serializers.ModelSerializer):
    block = serializers.CharField(source='block.block_id', read_only=True)
    class Meta:
        model = Transactions
        fields = ['block', 'owner_address', 'to_address', 'amount', 'txID']