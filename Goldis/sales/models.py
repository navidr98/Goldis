from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('buy_gold', 'Buying Gold'),
        ('sell_gold', 'Selling Gold'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    #card = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    seller = models.CharField(max_length=100, null=True, blank=True)
    rial_amount = models.DecimalField(max_digits=20, null=True , decimal_places=2)
    gold_amount = models.DecimalField(max_digits=20, null=True , decimal_places=4)
    price_per_gram = models.DecimalField(max_digits=20, null=True ,decimal_places=2)

    def __str__(self):
        return f"{self.transaction_type} - {self.transaction_id}"
