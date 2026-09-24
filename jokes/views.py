"""
In Django, views.py contains the core logic that processes HTTP requests and returns HTTP responses.  
It acts as the intermediary between models (data) and templates (user interface), determining what 
content is displayed to the user. 

Function-Based Views: Simple Python functions that accept a request and return a response, ideal for basic logic. 
Class-Based Views: Reusable classes that handle complex operations like CRUD (Create, Read, Update, Delete) 
with less boilerplate code. 

Integration: Views are mapped to URLs in urls.py and often render HTML templates with data fetched from models.
"""

from django.views.generic import DetailView, ListView

from .models import Joke

# By default, Django will be looking for joke_list.html
class JokeListView(ListView):
    model = Joke


class JokeDetailView(DetailView):
    model = Joke


