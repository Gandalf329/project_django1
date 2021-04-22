from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# sports_news
# Create your views here.
from django.views.generic import DetailView,UpdateView, DeleteView


def sports_home(request):
    news = Articles.objects.all()
    return render(request, 'sports/sports_home.html',{'news':news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'sports/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'sports/create.html'
    form_class = ArticlesForm
    
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/sports'
    template_name = 'sports/news-delete.html'
    

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sports')
        else:
            error = 'Form error'


    form = ArticlesForm()
    data = {
        'form':form,
        'error':error,
        }
# 2012-04-05 18:19:27
    return render(request,'sports/create.html',data)