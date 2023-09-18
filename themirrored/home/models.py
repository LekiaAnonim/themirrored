from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from blog.models import BlogPage, Category, WeeklyWordPage, HowPage, VideoPage


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']
    template = 'home/home_page.html'
    max_count = 1
    body = RichTextField(blank=True)
    site_name = models.CharField(null=True, blank=True, max_length=100)
    site_logo = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    mission = RichTextField(null=True)
    vision  = RichTextField(null=True)
    caption_main_text = models.CharField(null=True, blank=True, max_length=500)
    caption_sub_text = models.CharField(null=True, blank=True, max_length=500)
    caption_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('site_name'),
        FieldPanel('site_logo'),
        FieldPanel('mission'),
        FieldPanel('vision'),
        FieldPanel('caption_main_text'),
        FieldPanel('caption_sub_text'),
        FieldPanel('caption_image'),
    ]

    def __str__(self):
        return self.site_name
    
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        blogs = BlogPage.objects.all()
        recent_blogs = BlogPage.objects.all().order_by('date_created')[:4]
        article_of_the_week = BlogPage.objects.filter(article_of_the_week=True).order_by('date_created').first()
        videos = VideoPage.objects.all().order_by('date_created')[:6]
        how_of_the_week = HowPage.objects.filter(how_of_the_week=True).order_by('date_created').first()
        word_of_the_week = WeeklyWordPage.objects.filter(word_of_the_week=True).order_by('date_created').first()

        categories = Category.objects.all()
        context["blogs"] = blogs
        context["recent_blogs"] = recent_blogs
        context["videos"] = videos
        context["how_of_the_week"] = how_of_the_week
        context["word_of_the_week"] = word_of_the_week
        context["article_of_the_week"] = article_of_the_week
        context["categories"] = categories
        return context
    
class AboutPage(Page):
    template = 'home/about.html'
    max_count = 1
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    body = RichTextField(null=True)

    content_panels = Page.content_panels + [

        FieldPanel('image'),
        FieldPanel('body'),
    ]
