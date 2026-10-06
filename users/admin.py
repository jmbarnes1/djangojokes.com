from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

customUser = get_user_model()

# You must register CustomUserAdmin. You do this using the @admin.register decorator:
@admin.register(customUser)
class CustomUserAdmin(UserAdmin):
    model = customUser

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )

""""
The fieldsets and add_fieldsets properties hold the fieldsets that show up in Django admin’s forms:

fieldsets – These are the fieldsets used for updating existing records. Generally, you want this to contain all the 
fields that can be modified.

add_fieldsets – These are the fieldsets used for creating new records. This only needs to contain the 
required fields; however, it can contain additional fields that you generally want to have data for in new records.

fieldsets and add_fieldsets each holds a tuple, which itself contains one or more 2-element tuples:

The first element is the fieldset name (or None if the fieldset is unnamed).
The second element is a dictionary containing the CSS classes and the fields in the fieldset.
"""