from django.db import models

CHOOSE_MONEY_STATUS = (
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal')
)

class Investors(models.Model):
    full_name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='PROFILE_IMAGE')

    def __str__(self):
        return str(self.full_name)

class Financials(models.Model):
    investor = models.ForeignKey(Investors, on_delete=models.CASCADE)
    capital_invested = models.FloatField(default=0.0)
    market_value = models.FloatField(default=0.0)
    returns = models.FloatField(default=0.0)
    shareholder = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.investor)

class Ledger(models.Model):
    investor = models.ForeignKey(Investors, on_delete=models.CASCADE)
    money_moved = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(choices=CHOOSE_MONEY_STATUS, max_length=50, default='Deposit')

    def __str__(self):
        return str(self.id)

class Prometheus(models.Model):
    capital = models.FloatField(default=0.0)
    value = models.FloatField(default=0.0)
    returns = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)