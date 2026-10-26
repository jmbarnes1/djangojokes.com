"""
In Django, views.py contains the core logic that processes HTTP requests and returns HTTP responses.  
It acts as the intermediary between models (data) and templates (user interface), determining what 
content is displayed to the user. 

Function-Based Views: Simple Python functions that accept a request and return a response, ideal for basic logic. 
Class-Based Views: Reusable classes that handle complex operations like CRUD (Create, Read, Update, Delete) 
with less boilerplate code. 

Integration: Views are mapped to URLs in urls.py and often render HTML templates with data fetched from models.
"""
import json

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Joke

from .forms import JokeForm

# By default, Django will be looking for joke_list.html

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    # fields = ['question','answer'] # without form_class, this would build the form.  Now it goes to the joke form.
    form_class = JokeForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(UserPassesTestMixin, UpdateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

    def form_valid(self, form):
        messages.success(self.request, 'Joke deleted.')
        return super().form_valid(form)
    

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke


"""
Notice that we use reverse_lazy() here. The view is created before the URL 
configuration, so if you try to use reverse(), you will likely get an error 
about a circular import. The issue is that, with reverse(), the view needs 
the URLConf to have already been created, but the URLConf imports the view, so it cannot be created until the view exists.
"""