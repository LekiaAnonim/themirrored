from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel, MultiFieldPanel
from django.utils.functional import cached_property
from wagtail.fields import RichTextField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from cloudinary.models import CloudinaryField
# Create your models here.

from datetime import date
from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render
from blog.models import BlogPage, Video, HowPage, WeeklyWordPage, Category
from wagtailmetadata.models import MetadataPageMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class ResourceIndexPage(MetadataPageMixin, Page):
    template = 'resources/resource_list.html'
    intro = RichTextField(blank=True)
    banner = CloudinaryField("image", null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('banner')
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_resources = DownloadResourcesForm.objects.live().public().order_by('-first_published_at')
        print(all_resources)
        # Paginate all posts by 2 per page
        paginator = Paginator(all_resources, 6)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        print(posts)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        recent_blogs = BlogPage.objects.live().order_by('date_created')[:4]
        article_of_the_week = BlogPage.objects.live().filter(article_of_the_week=True).order_by('date_created').first()
        videos = Video.objects.all().order_by('date_created')[:6]
        how_of_the_week = HowPage.objects.live().filter(how_of_the_week=True).order_by('date_created').first()
        word_of_the_week = WeeklyWordPage.objects.live().filter(word_of_the_week=True).order_by('date_created').first()
        categories = Category.objects.live()
        context["recent_blogs"] = recent_blogs
        context["videos"] = videos
        context["how_of_the_week"] = how_of_the_week
        context["word_of_the_week"] = word_of_the_week
        context["article_of_the_week"] = article_of_the_week
        context["posts"] = posts
        return context

class FormField(AbstractFormField):
    page = ParentalKey('DownloadResourcesForm', on_delete=models.CASCADE, related_name='form_fields')


class DownloadResourcesForm(AbstractEmailForm, Page):
    template = 'resources/report.html'
    # year = models.CharField(max_length=4, blank=True, null=True)
    resource_title = models.CharField(max_length=500, blank=True, null=True)
    resource_summary = RichTextField(blank = True, null=True)
    resource_download_link = models.URLField(blank=True, null=True)
    resource_cover_image = CloudinaryField('image', null=True)
    thank_you_text = RichTextField(blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        # FieldPanel('year'),
        FieldPanel('resource_title'),
        FieldPanel('resource_summary'),
        FieldPanel('resource_download_link'),
        FieldPanel("resource_cover_image"),

        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(DownloadResourcesForm, self).get_context(request, *args, **kwargs)
        return context

    def get_form_fields(self):
        return self.form_fields.all()

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self)
            if form.is_valid():
                self.process_form_submission(form)
                addresses = [x.strip() for x in self.to_address.split(',')]
                # Subject can be adjusted (adding submitted date), be sure to include the form's defined subject field
                submitted_date_str = date.today().strftime('%x')
                subject = f"{self.subject} - {submitted_date_str}"
                # Update the original landing page context with other data
                context = self.get_context(request)

                text_content  = '\n' + '\n' + 'Dear,' + '\t' + str(form.cleaned_data['full_name']) + '\n' + '\n' +'\n'
                download_link = '<a href="{}" style="padding:10px; background:green; margin-top: 20px; color: white;">Download</a>'.format(self.report_download_link)
                html_content = render_to_string('reports/email_header.html', context, request=request)+text_content+render_to_string('reports/registration_email_template.html', context, request=request)+download_link

                msg = EmailMultiAlternatives(subject, text_content, self.from_address, [address for address in addresses]+[form.cleaned_data['email']])
                # msg.content_subtype = "html"  # Main content is now text/html
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                landing_page_context = self.get_context(request, *args, **kwargs)
                return render(
                    request,
                    self.get_landing_page_template(request),
                    landing_page_context
                )
        else:
            form = self.get_form(page=self)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )
    
