from django.shortcuts import render
from django.views import generic
from .models import Cell, Theme

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'latest_theme_list'

    def get_queryset(self):
        return Theme.objects.order_by('-pub_date')[:5]

class CommentsView(generic.DetailView):
    model = Theme
    template_name = 'comments/theme_comments.html'
