from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user

"""
The MyAccountPageView inherits from UpdateView.
You set model to get_user_model().
You set form_class to CustomUserChangeForm, which you just created.
You set template_name to 'account/my_account.html', which you will create shortly.
You override the superclass’s get_object() method
"""