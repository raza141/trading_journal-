from django.shortcuts import render, redirect, get_object_or_404
from .forms import TradeEntryForm  # Import the form
from .models import TradeEntry
from django.contrib import messages
from decimal import Decimal 

# View for adding a new trade entry
# def add_trade_entry(request):
#     if request.method == 'POST':
#         form = TradeEntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('journal_list')  # Redirect to the list of journal entries after saving
#     else:
#         form = TradeEntryForm()

#     return render(request, 'journal/add_trade_entry.html', {'form': form})


# View for editing an existing trade entry
def edit_trade_entry(request, pk):
    trade_entry = get_object_or_404(TradeEntry, pk=pk)

    if request.method == 'POST':
        form = TradeEntryForm(request.POST, instance=trade_entry)
        if form.is_valid():
            form.save()
            return redirect('journal_list')  # Redirect to list view after saving
    else:
        form = TradeEntryForm(instance=trade_entry)  # Populate form with existing entry

    return render(request, 'journal/edit_trade_entry.html', {'form': form, 'trade_entry': trade_entry})


def delete_trade_entry(request, pk):
    entry = get_object_or_404(TradeEntry, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('journal_list')
    return render(request, 'journal/confirm_delete.html', {'entry': entry})



def delete_trade_entry_by_id(request):
    if request.method == "POST":
        entry_id = request.POST.get("entry_id")
        try:
            entry = TradeEntry.objects.get(pk=entry_id)
            entry.delete()
            messages.success(request, f"Entry with ID {entry_id} deleted successfully.")
        except TradeEntry.DoesNotExist:
            messages.error(request, f"No entry found with ID {entry_id}.")
        return redirect('journal_list')

 # Import Decimal

def add_trade_entry(request):
    if request.method == 'POST':
        form = TradeEntryForm(request.POST)
        if form.is_valid():
            # Get the Entry Price and Risk/Reward Ratio
            entry_price = form.cleaned_data.get('entry_price')
            risk_reward_ratio = Decimal(form.cleaned_data.get('risk_reward_ratio'))  # Convert to Decimal
            risk_percentage = Decimal('0.01')  # Convert to Decimal for 1% risk

            # Calculate Stop Loss and Take Profit
            stop_loss = entry_price - (entry_price * risk_percentage)
            take_profit = entry_price + (entry_price * risk_percentage * risk_reward_ratio)

            # Save the form with calculated values
            trade_entry = form.save(commit=False)
            trade_entry.stop_loss = stop_loss
            trade_entry.take_profit = take_profit
            trade_entry.save()

            return redirect('journal_list')  # Redirect after saving
    else:
        form = TradeEntryForm()

    return render(request, 'journal/add_trade_entry.html', {'form': form})


# View for listing all journal entries
def journal_list(request):
    entries = TradeEntry.objects.all()  # Fetch all TradeEntry objects
    return render(request, 'journal/journal_list.html', {'entries': entries})
