from django import template
from blog.models import RequestFormSettings

register = template.Library()
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_request_form(context):
    request = context['request']
    print(request)
    request_form_settings = RequestFormSettings.for_request(request)
    request_form_page = request_form_settings.request_form_page.specific
    form = request_form_page.get_form(
        page=request_form_page, user=request.user)
    return {'page': request_form_page, 'form': form}