from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import *



class BlockDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    queryset = Block.objects.all()
    serializer_class = BlocksDetailSerializer
    lookup_field = 'block_id'



class TransactionDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    queryset = Transactions.objects.all()
    serializer_class = TransactionsDetailSerializer
    lookup_field = 'txID'

