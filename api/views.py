from .serializers import *
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny



class BlockDetailAPIView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    queryset = Block.objects.all()
    serializer_class = BlocksDetailSerializer
    lookup_field = 'block_id'
