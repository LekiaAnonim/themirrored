from django.db import models
from taggit.managers import TaggableManager
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from django.contrib.auth.models import AbstractUser
from wagtail.users.models import UserProfile
from django.urls import reverse
from django.shortcuts import render
from django.utils.text import slugify
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from django.conf import settings
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel, PageChooserPanel
import re
from wagtail.search import index
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

# class Writer(AbstractUser):
#     bio = models.TextField(null=True, blank=True)
#     facebook_url = models.URLField(max_length=500, null=True, blank=True)
#     twitter_url = models.URLField(max_length=500, null=True, blank=True)
#     instagram_url = models.URLField(max_length=500, null=True, blank=True)
#     threads_url = models.URLField(max_length=500, null=True, blank=True)
#     linkedin_url = models.URLField(max_length=500, null=True, blank=True)
#     youtube_url = models.URLField(max_length=500, null=True, blank=True)
class Category(Page):
    template = 'blog/category_blogs.html'
    name = models.CharField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name
    
    def get_context(self, request, *args, **kwargs):
        context = super(Category, self).get_context(request, *args, **kwargs)
        blogs = BlogPage.objects.filter(post_category = self.specific).order_by('date_created')
        context["blogs"] = blogs
        return context
    
@register_setting
class Author(BaseSiteSetting):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="post_user", null=True
    )
    bio = models.TextField(null=True, blank=True)
    facebook_url = models.URLField(max_length=500, null=True, blank=True)
    twitter_url = models.URLField(max_length=500, null=True, blank=True)
    instagram_url = models.URLField(max_length=500, null=True, blank=True)
    threads_url = models.URLField(max_length=500, null=True, blank=True)
    linkedin_url = models.URLField(max_length=500, null=True, blank=True)
    youtube_url = models.URLField(max_length=500, null=True, blank=True)

    slug = models.SlugField(null=True,  max_length=500)

    # content_panels = Page.content_panels + [
    #     FieldPanel('first_name'),
    #     FieldPanel('second_name'),
    #     FieldPanel('author_image'),
    #     FieldPanel('about_author'),
    #     FieldPanel('facebook_url'),
    #     FieldPanel('twitter_url'),
    #     FieldPanel('instagram_url'),
    #     FieldPanel('threads_url'),
    #     FieldPanel('linkedin_url'),
    #     FieldPanel('youtube_url'),
    # ]

    def __str__(self):
        return self.user.first_name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username, allow_unicode=True)
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:author_detail', kwargs={ 'slug': self.user.username})



class PostInfo(models.Model):
    post_title = models.CharField(
        max_length=500, null=True, help_text='Enter the title of your post')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    body = RichTextField(null=True)
    

    class Meta:
        abstract = True
        ordering = ['-date_created']

class BlogIndexPage(Page):
    template = 'blog/blog_list.html'
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class BlogPage(PostInfo, Page):
    post_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='post_author')
    post_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='post_category')
    article_of_the_week = models.BooleanField(default=False)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        index.SearchField('body'),
        index.FilterField('post_category'),
        index.FilterField('post_author'),
        index.FilterField('date_created'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('post_title'),
            FieldPanel('post_category'),
            FieldPanel('post_author'),
            # FieldPanel('date_created'),
            # FieldPanel('date_updated'),
            FieldPanel('tags'),
            FieldPanel('post_image'),
            FieldPanel('article_of_the_week'),
        ], heading="Post information"),
        
        FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        if self.article_of_the_week:
            BlogPage.objects.all().update(**{'article_of_the_week': False})
        super(BlogPage, self).save(*args, **kwargs)
    
# class BlogPageGalleryImage(Orderable):
#     page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
#     )
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]

class BlogTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class HowPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'HowPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class HowIndexPage(Page):
    template = 'blog/how_list.html'
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]  
class HowPage(PostInfo, Page):
    how_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='how_author')
    how_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='how_category')
    how_of_the_week = models.BooleanField(default=False)
    tags = ClusterTaggableManager(through=HowPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        index.SearchField('body'),
        index.FilterField('how_category'),
        index.FilterField('how_author'),
        index.FilterField('date_created'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('post_title'),
            FieldPanel('how_category'),
            FieldPanel('how_author'),
            # FieldPanel('date_created'),
            # FieldPanel('date_updated'),
            FieldPanel('tags'),
            FieldPanel('post_image'),
            FieldPanel('how_of_the_week'),
        ], heading="Post information"),
        
        FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title
    
    def save(self, *args, **kwargs):
        if self.how_of_the_week:
            HowPage.objects.all().update(**{'how_of_the_week': False})
        super(HowPage, self).save(*args, **kwargs)

class HowTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        howpages = HowPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['howpages'] = howpages
        return context


class WordPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'WeeklyWordPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class WeeklyWordIndexPage(Page):
    template = 'blog/word_list.html'
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ] 
class WeeklyWordPage(PostInfo, Page):
    word_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='word_author')
    word_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='word_category')
    word_of_the_week = models.BooleanField(default=False)
    tags = ClusterTaggableManager(through=WordPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        index.SearchField('body'),
        index.FilterField('word_category'),
        index.FilterField('word_author'),
        index.FilterField('date_created'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('post_title'),
            FieldPanel('word_category'),
            FieldPanel('word_author'),
            # FieldPanel('date_created'),
            # FieldPanel('date_updated'),
            FieldPanel('tags'),
            FieldPanel('post_image'),
            FieldPanel('word_of_the_week'),
        ], heading="Post information"),
        
        FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title
    
    def save(self, *args, **kwargs):
        if self.word_of_the_week:
            WeeklyWordPage.objects.all().update(**{'word_of_the_week': False})
        super(WeeklyWordPage, self).save(*args, **kwargs)

class WordTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        wordpages = WeeklyWordPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['wordpages'] = wordpages
        return context

# url = "https://youtu.be/wQSbQaSlG6s?si=f76aKaNUrEWnuYt-"
# match = re.search(r'^(https?://[^/]+/[^/]+/[^/]+)/', url)
# if match:
#     result = match.group(1)
#     print(result)
# else:
#     print("No match found.")
class VideoIndexPage(Page):
    template = 'blog/video_list.html'
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(VideoIndexPage, self).get_context(request, *args, **kwargs)
        videos = VideoPage.objects.all()
        context["videos"] = videos
        return context

class VideoPage(Page):
    template = 'blog/video_page.html'
    video_title = models.CharField(max_length=500, null=True)
    video_url = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('video_title'),
        FieldPanel('video_url'),
    ]
    def __str__(self):
        return self.video_title
    
    def save(self, *args, **kwargs):
        match = re.search(r'^(https?://[^/]+/[^/]+/[^/]+)/', self.video_url)
        self.video_url = match.group(1)
        super(VideoPage, self).save(*args, **kwargs)


@register_setting
class SiteSocial(BaseSiteSetting):
    facebook = models.URLField(max_length=500, null=True, blank=True)
    twitter = models.URLField(max_length=500, null=True, blank=True)
    instagram = models.URLField(max_length=500, null=True, blank=True)
    threads = models.URLField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=500, null=True, blank=True)
    youtube = models.URLField(max_length=500, null=True, blank=True)
    tiktok = models.URLField(max_length=500, null=True, blank=True)

@register_setting
class SiteContact(BaseSiteSetting):
    email1 = models.EmailField(help_text='Your Email address', null=True, blank=True)
    email2 = models.EmailField(help_text='Your Email address', null=True, blank=True)
    email3 = models.EmailField(help_text='Your Email address', null=True, blank=True)
    phone1 = PhoneNumberField(null=True, blank=True)
    phone2 = PhoneNumberField(null=True, blank=True)
    phone3 = PhoneNumberField(null=True, blank=True)

@register_setting
class SiteLogo(BaseSiteSetting):
    logo = models.ImageField(null=True, blank=True)
    favicon = models.ImageField(null=True, blank=True)

@register_setting
class ImportantPages(BaseSiteSetting):
    # Fetch these pages when looking up ImportantPages for or a site
    select_related = ["blog_index_page", "about_page", "how_index_page", "word_index_page", "video_index_page"]

    blog_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')
    about_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')
    how_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')
    word_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    # contact_page = models.ForeignKey(
    #     'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    video_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        PageChooserPanel('blog_index_page', ['blog.BlogIndexPage']),
        PageChooserPanel('about_page', ['home.AboutPage']),
        PageChooserPanel('how_index_page', ['blog.HowIndexPage']),
        PageChooserPanel('word_index_page', ['blog.HowIndexPage']),
        PageChooserPanel('video_index_page', ['blog.VideoIndexPage']),
        # PageChooserPanel('contact_page', ['blog.ContactPage']),
    ]


@register_snippet
class SiteEmails(models.Model):
    emails = models.EmailField(max_length = 500, null=True, blank=True)
    panels = [
        FieldPanel('emails'),
    ]

    def __str__(self):
        return self.emails
    

class FormField(AbstractFormField):
    page = ParentalKey('RequestFormPage', on_delete=models.CASCADE, related_name='form_fields')

class RequestFormPage(AbstractEmailForm):
    template = 'blog/request_form.html'
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
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

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)

            if form.is_valid():
                self.process_form_submission(form)
                
                # Update the original landing page context with other data
                landing_page_context = self.get_context(request)
                landing_page_context['first_name'] = form.cleaned_data['first_name']

                return render(
                    request,
                    self.get_landing_page_template(request),
                    landing_page_context
                )
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.get_template(request),
            context
        )

@register_setting
class RequestFormSettings(BaseSiteSetting):
    request_form_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

    panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('request_form_page', ['blog.RequestFormPage']),
    ]
