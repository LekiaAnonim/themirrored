# from django import forms
# from django.utils.translation import gettext_lazy as _

# from wagtail.users.forms import UserEditForm, UserCreationForm

# # from blog.models import MembershipStatus
# from wagtail.images import get_image_model
# from wagtail.images.widgets import AdminImageChooser
# from wagtail.users.forms import UserCreationForm, UserEditForm

# class CustomUserEditForm(UserEditForm):
#     avatar = forms.ModelChoiceField(
#         queryset=get_image_model().objects.all(), widget=AdminImageChooser(),
#     )
#     bio = forms.CharField(widget=forms.Textarea, required=False, label=_("Bio"))
#     facebook_url = forms.URLField()
#     twitter_url = forms.URLField()
#     instagram_url = forms.URLField()
#     threads_url = forms.URLField()
#     linkedin_url = forms.URLField()
#     youtube_url = forms.URLField()


# class CustomUserCreationForm(UserCreationForm):
#     avatar = forms.ModelChoiceField(
#         queryset=get_image_model().objects.all(), widget=AdminImageChooser(),
#     )
#     bio = forms.CharField(widget=forms.Textarea, required=False, label=_("Bio"))
#     facebook_url = forms.URLField()
#     twitter_url = forms.URLField()
#     instagram_url = forms.URLField()
#     threads_url = forms.URLField()
#     linkedin_url = forms.URLField()
#     youtube_url = forms.URLField()


# from django import forms
# from wagtail.users.models import UserProfile
# from blog.models import User

# class CustomSettingsForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['avatar', 'bio', 'facebook_url', 'twitter_url', 'instagram_url', 'threads_url', 'linkedin_url', 'youtube_url']