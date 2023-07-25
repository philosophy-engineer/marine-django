from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountUpdateForm
from django.urls import reverse_lazy, reverse
from .models import HelloWorld
from django.http import HttpResponseRedirect
# import pdb


def hello_world(request):
    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello-world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # succequss_url = '/account/hello-world/'
    # pdb.set_trace()
    success_url = reverse_lazy('accountapp:hello-world')
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "accountapp/detail.html"


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello-world')
    template_name = "accountapp/update.html"


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello-world')
    template_name = "accountapp/delete.html"
    