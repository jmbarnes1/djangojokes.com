import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email

from .models import Applicant
from .forms import JobApplicationForm
# Create your views here.

class JobAppView(CreateView):
    # template_name = 'jobs/joke_writer.html' # indetifies the template used to render the form.
    model = Applicant
    form_class = JobApplicationForm # indentifies the form class, which contains the form fields.
    success_url = reverse_lazy('jobs:thanks') # points to the URL to open when the form is successfully processed.

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'you@example.com'
        subject = 'Application for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)


class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html' # success_url from above needs a place to go. 