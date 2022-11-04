from django.shortcuts import render
from django.views import generic
from .models import Cell

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'latest_cell_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Cell.objects.order_by('-pub_date')[:5]
