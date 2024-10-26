from django import forms
from .models import TradeEntry

class TradeEntryForm(forms.ModelForm):
    class Meta:
        model = TradeEntry
        fields = [
            'market', 'country', 'ticker', 'identify_date', 'strategy', 'macro_event', 'entry_date',
            'entry_price', 'position_size', 'exit_date', 'exit_price','status',
            'capital', 'technicals', 'fundamentals', 'stop_loss', 'take_profit', 
            'risk_reward_ratio', 'pre_trade_emotions', 'in_trade_emotions',
            'post_trade_emotions', 'lessons_learned'
        ]
        # Adding widgets for styling and ease of use
        widgets = {
            'identify_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'entry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'exit_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'market': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'strategy': forms.TextInput(attrs={'placeholder': 'BUY-HOLD','class': 'form-control'}),
            'macro_event': forms.TextInput(attrs={'placeholder': 'Earning report','class': 'form-control'}),
            'ticker': forms.TextInput(attrs={'placeholder': 'BOP','class': 'form-control'}),
            'entry_price': forms.NumberInput(attrs={'placeholder': '100','class': 'form-control'}),
            'exit_price': forms.NumberInput(attrs={'placeholder': '100','class': 'form-control'}),
            'position_size': forms.NumberInput(attrs={'placeholder': 'Number of Shares','class': 'form-control'}),
            'capital': forms.NumberInput(attrs={'placeholder': '10,000', 'class': 'form-control'}),
            'stop_loss': forms.NumberInput(attrs={'class': 'form-control'}),
            'take_profit': forms.NumberInput(attrs={'class': 'form-control'}),
            'risk_reward_ratio': forms.NumberInput(attrs={'placeholder': '1:2','class': 'form-control'}),
            'technicals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fundamentals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pre_trade_emotions': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'in_trade_emotions': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'post_trade_emotions': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'lessons_learned': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
