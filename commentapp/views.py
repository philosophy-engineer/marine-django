from django.views.generic import CreateView, DeleteView
from django.urls import reverse
from .models import Comment
from .forms import CommentCreationForm
from articleapp.models import Article
from django.utils.decorators import method_decorator
from .decorators import comment_ownership_required



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        tmp_comment = form.save(commit=False)
        tmp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        tmp_comment.writer = self.request.user
        tmp_comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

