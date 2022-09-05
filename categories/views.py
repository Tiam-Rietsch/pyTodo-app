from django.db import IntegrityError
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Category


class CategoryListView(LoginRequiredMixin, ListView,):
    model = Category
    template_name = 'categories/category_list.html'
    login_url = 'login'


    def get_context_data(self):
        cat_list = Category.objects.filter(author=self.request.user).order_by('progress')
        
        context = {
            "cat_list":cat_list
        }
        return context


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'categories/category_create.html'
    fields = ('title', 'description',)
    success_url = reverse_lazy('cat_list')
    login_url = 'login'
    

    # strip and remove all alpha characters from a string
    def replace_characters(self, s):
        s2 = "".join(c for c in s if c.isalpha() or c == " ")
        return s2
    

    def form_valid(self, form):
        try:
            form.instance.title = self.replace_characters(form.instance.title)
            form.instance.author = self.request.user
            form.instance.user_title = self.request.user.username + '-' + form.instance.title
            slug_text = '-'.join(str.split(form.instance.user_title))
            form.instance.slug = slug_text + '-cat'
            return super().form_valid(form)
        except IntegrityError:
            return render(self.request, 'pages/errors.html', {"name":form.instance.title})
    
        


class CategoryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    


class DeleteCategoryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('cat_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'categories/category_update.html'
    fields = ('title', 'description')
    login_url = 'login'
    
    def get_success_url(self):
        obj = self.get_object()
        self.success_url = reverse_lazy('cat_detail', kwargs={'slug': obj.slug})
        return super().get_success_url()

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
