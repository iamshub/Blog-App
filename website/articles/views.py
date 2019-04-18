from django.views.generic import ListView, DetailView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'home1.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class A1(ListView):
    model = Article
    template_name = 'home.html'




class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'



    
