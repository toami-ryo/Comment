from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Cell, Theme
from .forms import ContributeForm
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'latest_theme_list'

    def get_queryset(self):
        return Theme.objects.order_by('-pub_date')[:5]



def CommentsView(request, theme_id):
    template_name = 'comments/theme_comments.html'
    theme = get_object_or_404(Theme, pk = theme_id)

    context = {'theme':theme,
               'contribute_form':ContributeForm()}

    return render(request, template_name, context)

def contribute(request, theme_id):
    template_name = 'comments/theme_comments.html'
    theme = get_object_or_404(Theme, pk = theme_id)
    context = {'theme':theme}

    publisher_name = request.POST['publisher_name']
    comment_text = request.POST['comment_text']
    pub_date = datetime.now()
    Cell.objects.create(theme=theme, 
                        publisher_name=publisher_name, 
                        comment_text=comment_text,
                        pub_date=pub_date)
    
    # フォームをクリアしながらmodelを反映させるリダイレクト
    return redirect(f'/comments/{theme_id}/')






