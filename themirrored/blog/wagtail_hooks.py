# wagtail_hooks.py

from wagtail.admin.views.account import BaseSettingsPanel
from wagtail import hooks
from .forms import CustomSettingsForm

@hooks.register('register_account_settings_panel')
class CustomSettingsPanel(BaseSettingsPanel):
    name = 'Author Profile'
    title = "Author Profile Settings"
    order = 500
    form_class = CustomSettingsForm
    form_object = 'profile'