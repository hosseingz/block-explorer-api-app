from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('get-block/<block_id>', views.BlockDetailAPIView.as_view(), name='block_detail'),
    path('get-transaction/<txID>', views.TransactionDetailAPIView.as_view(), name='transaction_detail'),
]