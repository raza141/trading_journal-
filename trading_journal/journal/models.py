from django.db import models
from datetime import date


class TradeEntry(models.Model):
    STATUS_CHOICES = [
        ('Trailing_SL', 'Trailing SL'),
        ('Stop_loss_hit', 'Stop loss hit'),
        ('Running_profits', 'Running profits'),
        ('Target_hit', 'Target hit'),
        ('Near_target', 'Near target'),
        ('Waiting_for_entry', 'Waiting for ENTRY signal'),
        ('Holding', 'Holding'),
        ('Near_stop_loss', 'Near Stop Loss'),
    ]
    MARKET_CHOICES = [
        ('Equity', 'Equity'),
        ('Fixed_Income', 'Fixed Income'),
        ('Commodities', 'Commodities'),
        ('Crypto', 'Crypto'),
        ('Forex', 'Forex'),
    ]

    COUNTRY_CHOICES = [
        ('USA', 'USA'),
        ('PAK', 'PAK'),
        ('UAE', 'UAE'),
    ]

    TRADE_EMOTION_CHOICES = [
        ('Confident', 'Confident'),
        ('Excited', 'Excited'),
        ('Nervous', 'Nervous'),
        ('Fearful', 'Fearful'),
        ('Greedy', 'Greedy'),
        ('Impatient', 'Impatient'),
        ('Relaxed', 'Relaxed'),
        ('Doubtful', 'Doubtful'),
        ('Indifferent', 'Indifferent'),
        ('Optimistic', 'Optimistic'),
        ('Pessimistic', 'Pessimistic'),
        ('Overconfident', 'Overconfident'),
        ('Curious', 'Curious'),
    ]
    # trade_id = models.AutoField(primary_key=True, default=1)
    market = models.CharField(max_length=20, choices=MARKET_CHOICES, default='Equity')
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default='PAK')
    ticker = models.CharField(max_length=10)
    identify_date = models.DateField(null=True, blank=True)
    strategy = models.CharField(max_length=255)
    entry_date = models.DateField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    position_size = models.IntegerField()
    exit_date = models.DateField(null=True, blank=True)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    days = models.IntegerField(editable=False, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Waiting_for_entry')
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    technicals = models.TextField(null=True, blank=True)
    fundamentals = models.TextField(null=True, blank=True)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2)
    take_profit = models.DecimalField(max_digits=10, decimal_places=2)
    risk_reward_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    profit_loss = models.DecimalField(max_digits=15, decimal_places=2, editable=False, null=True)
    pre_trade_emotions = models.CharField(max_length=20, choices=TRADE_EMOTION_CHOICES, default='Confident', null=True, blank=True)
    in_trade_emotions = models.CharField(max_length=20, choices=TRADE_EMOTION_CHOICES, default='Confident', null=True, blank=True)
    post_trade_emotions = models.CharField(max_length=20, choices=TRADE_EMOTION_CHOICES, default='Confident', null=True, blank=True)
    lessons_learned = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.date} - {self.ticker} - {self.status}"



    def calculate_days(self):
        """Calculate the number of days from entry_date to exit_date (or today if no exit_date)."""
        if self.exit_date:
            return (self.exit_date - self.entry_date).days
        else:
            return (date.today() - self.entry_date).days    

    def calculate_profit_loss(self):
        """Calculate profit/loss based on exit and entry prices."""
        if self.exit_price and self.entry_price:
            # Formula: (Exit Price - Entry Price) * Position Size
            return round((self.exit_price - self.entry_price) * self.position_size, 2)
        return None  # Return None if exit_price is not available

    def save(self, *args, **kwargs):
        """Override save to auto-calculate days based on entry_date and exit_date."""
        self.days = self.calculate_days()  # Automatically set 'days' field
        self.profit_loss = self.calculate_profit_loss()
        super().save(*args, **kwargs)