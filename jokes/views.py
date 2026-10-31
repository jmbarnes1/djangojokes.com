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
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Joke, JokeVote
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



def vote(request, slug):
    user = request.user # The logged-in user (or AnonymousUser).
    joke = Joke.objects.get(slug=slug) # The joke instance.
    data = json.loads(request.body) # Data from the JavaScript.

    # Set simple variables.
    vote = data['vote'] # The user's new vote.
    likes = data['likes'] # The number of likes currently displayed on page.
    dislikes = data['dislikes'] # The number of dislikes currently displayed.

    if user.is_anonymous: # User not logged in. Can't vote.
        msg = 'Sorry, you have to be logged in to vote.'
    else: # User is logged in.
        if JokeVote.objects.filter(user=user, joke=joke).exists():
            # User already voted. Get user's past vote:
            joke_vote = JokeVote.objects.get(user=user, joke=joke)

            if joke_vote.vote == vote: # User's new vote is the same as old vote.
                msg = 'Right. You told us already. Geez.'
            else: # User changed vote.
                joke_vote.vote = vote # Update JokeVote instance.
                joke_vote.save() # Save.

                # Set data to return to the browser.
                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "Don't like it after all, huh? OK. Noted."
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'Grown on you, has it? OK. Noted.'
        else: # First time user is voting on this joke.
            # Create and save new vote.
            joke_vote = JokeVote(user=user, joke=joke, vote=vote)
            joke_vote.save()

            # Set data to return to the browser.
            if vote == -1:
                dislikes += 1
                msg = "Sorry you didn't like the joke."
            else:
                likes += 1
                msg = "Yeah, good one, right?"

    # Create object to return to browser.
    response = {
        'msg': msg,
        'likes': likes,
        'dislikes': dislikes
    }
    return JsonResponse(response) # Return object as JSON.