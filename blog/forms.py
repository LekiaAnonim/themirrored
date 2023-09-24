from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

# from blog.models import MembershipStatus


class CustomUserEditForm(UserEditForm):
    # avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea, required=False, label=_("Bio"))
    facebook_url = forms.URLField()
    twitter_url = forms.URLField()
    instagram_url = forms.URLField()
    threads_url = forms.URLField()
    linkedin_url = forms.URLField()
    youtube_url = forms.URLField()


class CustomUserCreationForm(UserCreationForm):
    # avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea, required=False, label=_("Bio"))
    facebook_url = forms.URLField()
    twitter_url = forms.URLField()
    instagram_url = forms.URLField()
    threads_url = forms.URLField()
    linkedin_url = forms.URLField()
    youtube_url = forms.URLField()


# forms.py

from django import forms
from wagtail.users.models import UserProfile
from blog.models import Author

class CustomSettingsForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['bio', 'facebook_url', 'twitter_url', 'instagram_url', 'threads_url', 'linkedin_url', 'youtube_url']