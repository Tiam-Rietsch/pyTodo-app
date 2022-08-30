from http.client import HTTPResponse
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm, TaskResetForm
from categories.models import Category


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    form_class = TaskCreateForm
    login_url = 'login'

    # Authomatically set the author and the category under which the task falls depending on the url slugs
    def form_valid(self, form):
        form.instance.author = self.request.user
        cat = Category.objects.get(slug=self.kwargs.get('slug')) # get the Category Instance using the slug from the url 
        form.instance.category = cat
        
        return super().form_valid(form)  


    # redirect the user the cat_detail template after success
    def get_success_url(self):        
        self.success_url = reverse_lazy('cat_detail', kwargs={'slug': self.kwargs.get('slug')})
        return super().get_success_url()
    
    # prevents a user from creating a task in another user's account
    def test_func(self):
        cat = Category.objects.get(slug=self.kwargs.get('slug'))
        return cat.author == self.request.user


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    login_url = 'login'

    # redirect the user to the cat_list template
    def get_success_url(self):        
        obj = Task.objects.get(pk=self.kwargs.get('pk'))
        self.success_url = reverse_lazy('cat_detail', kwargs={'slug':obj.category.slug})
        return super().get_success_url()

    # test whether the actual user is the author of the task, to be able to delete the task
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model =    Task
    template_name = 'tasks/task_update.html'
    form_class = TaskUpdateForm
    login_url = 'login'

    def get_success_url(self):
        obj = self.get_object()
        self.success_url = reverse_lazy('cat_detail', kwargs={'slug':obj.category.slug})
        return super().get_success_url()


    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
    

class TaskResetView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_reset.html'
    form_class = TaskResetForm
    login_url = 'login'

    def get_success_url(self):
        obj = self.get_object()
        self.success_url = reverse_lazy('cat_detail', kwargs={'slug': obj.category.slug})
        return super().get_success_url()

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        form.instance.completed = False
        return super().form_valid(form)