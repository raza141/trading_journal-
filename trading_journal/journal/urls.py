from django.urls import path
from . import views



urlpatterns = [
    path('', views.journal_list, name='journal_list'),  # List all entries
    path('add/', views.add_trade_entry, name='add_trade_entry'),  # URL for adding new entry
    path('edit/<int:pk>/', views.edit_trade_entry, name='edit_trade_entry'),  # URL for editing
]
