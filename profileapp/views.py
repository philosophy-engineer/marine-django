# from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import Profile
from .forms import ProfileCreationForm
from django.utils.decorators import method_decorator
from .decorators import profile_ownership_required

# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    
    def form_valid(self, form):
        tmp_profile = form.save(commit=False)
        tmp_profile.user = self.request.user
        tmp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

    
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    