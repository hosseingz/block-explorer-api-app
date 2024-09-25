from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    # path('login/'),
    
    path('get-block/<block_id>', views.BlockDetailAPIView.as_view(), name='block_detail'),
    path('get-transaction/<txID>', views.TransactionDetailAPIView.as_view(), name='transaction_detail'),
    path('get-address-transactions/<address>', views.AddressAPIView.as_view(), name='transaction_detail'),
]