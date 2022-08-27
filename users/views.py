from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        new_user = authenticate(
            username = form.cleaned_data["username"],
            password = form.cleaned_data["password1"]
        )
        login(self.request, new_user)
        return HttpResponseRedirect(reverse_lazy('cat_list'))