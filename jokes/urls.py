"""
Django's urls.py file serves as the application's routing map, responsible for mapping incoming web 
request URLs to their corresponding views (Python functions or classes).  When a user requests a page, 
Django's URL resolver scans the urlpatterns list defined in urls.py to find the first matching pattern 
and then executes the associated view to generate the response. 

To maintain code organization and reusability, Django projects typically use a root urls.py that includes 
app-specific URLs using the include() function.  This allows each app to manage its own routes in a separate 
urls.py file, keeping the main project file clean and enabling apps to be easily plugged into different projects. 
Key functions like path() and re_path() are used to define these routes, supporting both static paths and dynamic 
parameters captured from the URL. 
"""

from django.urls import path

# Look in the current directory (denoted by .). 
# Import the module named views (which corresponds to the file views.py). 
# Retrieve the specific class or function named JokeListView from that module.
from .views import JokeListView


"""
Application Namespace: The variable app_name = 'jokes' sets the application namespace to jokes. 
This allows for unique URL reverse resolution (e.g., reverse('jokes:list')) when multiple apps might have URLs 
with the same name.

URL Pattern List: The urlpatterns list contains the routing rules for this specific app. 

Root Path Mapping: The entry path('', JokeListView.as_view(), name='list') maps the empty string '' (representing 
the base URL of this app, e.g., /jokes/ if included under that prefix) to the JokeListView.

Class-Based View: JokeListView.as_view() converts the class-based view into a callable view function that 
Django can handle. 

URL Name: The name='list' argument assigns the name list to this URL pattern, enabling reverse lookups 
within templates or views using the application namespace.
"""

app_name = 'jokes'
urlpatterns = [
    path('',JokeListView.as_view(),name='list'),
]