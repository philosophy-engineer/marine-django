# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Article
from .forms import ArticleCreationForm
from .decorators import article_ownership_required

# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        tmp_article = form.save(commit=False)
        tmp_article.writer = self.request.user
        tmp_article.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

    
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})
    
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')
    