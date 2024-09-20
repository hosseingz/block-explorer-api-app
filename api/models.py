from django.db import models



class Block(models.Model):
    block_id = models.CharField(max_length=128)
    timestamp = models.CharField(max_length=128)

    def __str__(self):
        return str(self.block_id)
    

class Transactions(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='transactions')
    owner_address = models.CharField(max_length=128, verbose_name='from')
    to_address = models.CharField(max_length=128)
    amount = models.DecimalField(default=0, max_digits=30, decimal_places=2)
    txID = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.owner_address[:8]} - {self.to_address[:8]} : {self.amount}'
    
    