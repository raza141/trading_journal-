from django.shortcuts import render, redirect, get_object_or_404
from .forms import TradeEntryForm  # Import the form
from .models import TradeEntry

# View for adding a new trade entry

# View for adding a new trade entry
def add_trade_entry(request):
    if request.method == 'POST':
        form = TradeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_list')  # Redirect to the list of journal entries after saving
    else:
        form = TradeEntryForm()

    return render(request, 'journal/add_trade_entry.html', {'form': form})


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



# View for listing all journal entries
def journal_list(request):
    entries = TradeEntry.objects.all()  # Fetch all TradeEntry objects
    return render(request, 'journal/journal_list.html', {'entries': entries})
