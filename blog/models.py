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
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
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
from blog.utils.blog_utils import count_words, read_time
from wagtail.snippets.models import register_snippet
from cloudinary.models import CloudinaryField
from wagtailmetadata.models import MetadataPageMixin
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from resources.models import ResourceIndexPage
# Create your models here.
AUTH_USER = settings.AUTH_USER_MODEL

class Author(Page):
    template = 'blog/author_detail.html'
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="author",
    )
    bio = models.TextField(null=True, blank=True)
    facebook_url = models.URLField(max_length=500, null=True, blank=True)
    twitter_url = models.URLField(max_length=500, null=True, blank=True)
    instagram_url = models.URLField(max_length=500, null=True, blank=True)
    threads_url = models.URLField(max_length=500, null=True, blank=True)
    linkedin_url = models.URLField(max_length=500, null=True, blank=True)
    youtube_url = models.URLField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [

        FieldPanel('user'),
        FieldPanel('bio'),
        FieldPanel('facebook_url'),
        FieldPanel('twitter_url'),
        FieldPanel('instagram_url'),
        FieldPanel('threads_url'),
        FieldPanel('linkedin_url'),
        FieldPanel('youtube_url'),
    ]

    class Meta:
        verbose_name = _("Author profile")
        verbose_name_plural = _("Author profiles")

    def save(self, *args, **kwargs):
        self.user = self.specific.owner
        super(Author, self).save(*args, **kwargs)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
class Category(MetadataPageMixin, Page):
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
    
# @register_setting
# class Author(BaseSiteSetting):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="post_user", null=True
#     )
#     bio = models.TextField(null=True, blank=True)
#     facebook_url = models.URLField(max_length=500, null=True, blank=True)
#     twitter_url = models.URLField(max_length=500, null=True, blank=True)
#     instagram_url = models.URLField(max_length=500, null=True, blank=True)
#     threads_url = models.URLField(max_length=500, null=True, blank=True)
#     linkedin_url = models.URLField(max_length=500, null=True, blank=True)
#     youtube_url = models.URLField(max_length=500, null=True, blank=True)

#     slug = models.SlugField(null=True,  max_length=500)

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

    # def __str__(self):
    #     return self.user.first_name
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.user.username, allow_unicode=True)
    #     super(Author, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('blog:author_detail', kwargs={ 'slug': self.user.username})

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class PostInfo(models.Model):
    post_title = models.CharField(
        max_length=500, null=True, blank=True, help_text='Enter the title of your post')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_image = CloudinaryField("image", null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    allow_comments = models.BooleanField('allow comments', default=True)
    

    class Meta:
        abstract = True
        ordering = ['-date_created']

class BlogIndexPage(MetadataPageMixin, Page):
    template = 'blog/blog_list.html'
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
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 6)
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
    


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )
class BlogPage(MetadataPageMixin, PostInfo, Page):
    template = 'blog/blog_page.html'
    post_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='post_author')
    post_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='post_category')
    article_of_the_week = models.BooleanField(default=False)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    read_time = models.CharField(max_length=50, default=0)
    views = models.ManyToManyField(IpModel, related_name="blog_views", blank=True)
    likes = models.ManyToManyField(IpModel, related_name="blog_likes", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        index.SearchField('body'),
        index.FilterField('post_category'),
        # index.FilterField('post_author'),
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
            FieldPanel('allow_comments'),
        ], heading="Post information"),
        
        FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title
    
    def total_views(self):
        return self.views.count()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return self.get_url()

    def save(self, *args, **kwargs):
        self.read_time = read_time(self.body)
        self.post_author = self.owner.author
        if self.article_of_the_week:
            BlogPage.objects.all().update(**{'article_of_the_week': False})
        super(BlogPage, self).save(*args, **kwargs)
    
    # write a get_context method
    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        related_content = []
        if self.tags:
            for tag in self.tags.all():
                related_content += BlogPage.objects.live().filter(tags__name=tag)
                related_content += HowPage.objects.live().filter(tags__name=tag)
                related_content += WeeklyWordPage.objects.live().filter(tags__name=tag)
        else:
            return related_content
        
        context["related_content"] = related_content
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # adding like count
        like_status = False
        ip = get_client_ip(request)
        if self.object.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
            like_status = True
        else:
            like_status=False
        context['like_status'] = like_status


        return self.render_to_response(context)

class BlogTagIndexPage(MetadataPageMixin, Page):
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
class HowIndexPage(MetadataPageMixin, Page):
    template = 'blog/how_list.html'
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
        all_posts = HowPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 6)
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
class HowPage(MetadataPageMixin, PostInfo, Page):
    how_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='how_author')
    how_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='how_category')
    how_of_the_week = models.BooleanField(default=False)
    tags = ClusterTaggableManager(through=HowPageTag, blank=True)
    read_time = models.CharField(max_length=50, default=0)
    views = models.ManyToManyField(IpModel, related_name="how_views", blank=True)
    likes = models.ManyToManyField(IpModel, related_name="how_likes", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        index.SearchField('body'),
        index.FilterField('how_category'),
        # index.FilterField('how_author'),
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
            FieldPanel('allow_comments'),
        ], heading="Post information"),
        
        FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title

    def total_views(self):
        return self.views.count()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return self.get_url()
    
    def save(self, *args, **kwargs):
        self.read_time = read_time(self.body)
        self.how_author = self.owner.author
        if self.how_of_the_week:
            HowPage.objects.all().update(**{'how_of_the_week': False})
        super(HowPage, self).save(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # adding like count
        like_status = False
        ip = get_client_ip(request)
        if self.object.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
            like_status = True
        else:
            like_status=False
        context['like_status'] = like_status


        return self.render_to_response(context)

class HowTagIndexPage(MetadataPageMixin, Page):
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
class WeeklyWordIndexPage(MetadataPageMixin, Page):
    template = 'blog/word_list.html'
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
        all_posts = WeeklyWordPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 6)
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
class WeeklyWordPage(MetadataPageMixin, PostInfo, Page):
    # word_author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='word_author')
    # word_category = ParentalKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='word_category')
    word_of_the_week = models.BooleanField(default=False)
    # tags = ClusterTaggableManager(through=WordPageTag, blank=True)
    read_time = models.CharField(max_length=50, default=0)
    views = models.ManyToManyField(IpModel, related_name="word_views", blank=True)
    likes = models.ManyToManyField(IpModel, related_name="word_likes", blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('post_title'),
        # index.SearchField('body'),
        # index.FilterField('word_category'),
        # index.FilterField('word_author'),
        index.FilterField('date_created'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            # FieldPanel('post_title'),
            # FieldPanel('word_category'),
            # FieldPanel('word_author'),
            # FieldPanel('tags'),
            FieldPanel('post_image'),
            FieldPanel('word_of_the_week'),
            FieldPanel('allow_comments'),
        ], heading="Post information"),
        
        # FieldPanel('body'),
        # InlinePanel('gallery_images', label="Gallery images"),
    ]

    def __str__(self):
        return self.post_title
    
    def total_views(self):
        return self.views.count()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return self.get_url()
    
    def save(self, *args, **kwargs):
        self.read_time = read_time(self.body)
        self.word_author = self.owner.author
        if self.word_of_the_week:
            WeeklyWordPage.objects.all().update(**{'word_of_the_week': False})
        super(WeeklyWordPage, self).save(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # adding like count
        like_status = False
        ip = get_client_ip(request)
        if self.object.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
            like_status = True
        else:
            like_status=False
        context['like_status'] = like_status


        return self.render_to_response(context)
class WordTagIndexPage(MetadataPageMixin, Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        wordpages = WeeklyWordPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['wordpages'] = wordpages
        return context

def blogLike(request, pk):
    postid = request.POST.get('blogid')
    post = get_object_or_404(BlogPage, pk=postid)
    ip = get_client_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.likes.remove(IpModel.objects.get(ip=ip))
    else:
        post.likes.add(IpModel.objects.get(ip=ip))
    return redirect(post)


def howLike(request, pk):
    postid = request.POST.get('blogid')
    post = get_object_or_404(HowPage, pk=postid)
    ip = get_client_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.likes.remove(IpModel.objects.get(ip=ip))
    else:
        post.likes.add(IpModel.objects.get(ip=ip))
    return redirect(post)

def wordLike(request, pk):
    postid = request.POST.get('blogid')
    post = get_object_or_404(WeeklyWordPage, pk=postid)
    ip = get_client_ip(request)
    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.likes.remove(IpModel.objects.get(ip=ip))
    else:
        post.likes.add(IpModel.objects.get(ip=ip))
    return redirect(post)

# url = "https://youtu.be/wQSbQaSlG6s?si=f76aKaNUrEWnuYt-"
# match = re.search(r'^(https?://[^/]+/[^/]+/[^/]+)/', url)
# if match:
#     result = match.group(1)
#     print(result)
# else:
#     print("No match found.")
class VideoIndexPage(MetadataPageMixin, Page):
    template = 'blog/video_list.html'
    intro = RichTextField(blank=True)
    banner = CloudinaryField("image", null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('banner')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(VideoIndexPage, self).get_context(request, *args, **kwargs)
        videos = Video.objects.all()
        context["videos"] = videos
        return context

@register_snippet
class Video(models.Model):
    video_title = models.CharField(max_length=500, null=True)
    video_url = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    panels = [
        FieldPanel('video_title'),
        FieldPanel('video_url'),
    ]
    def __str__(self):
        return self.video_title
    
    def save(self, *args, **kwargs):
        match = re.search(r'youtu.be/([^/]+)', self.video_url)
        self.video_url = match.group(1)
        super(Video, self).save(*args, **kwargs)


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
    logo = CloudinaryField("image", null=True)
    favicon = CloudinaryField("image", null=True)

@register_setting
class ImportantPages(BaseSiteSetting):
    # Fetch these pages when looking up ImportantPages for or a site
    select_related = ["blog_index_page", "about_page", "how_index_page", "word_index_page", "resources_index_page"]

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

    resources_index_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        PageChooserPanel('blog_index_page', ['blog.BlogIndexPage']),
        PageChooserPanel('about_page', ['home.AboutPage']),
        PageChooserPanel('how_index_page', ['blog.HowIndexPage']),
        PageChooserPanel('word_index_page', ['blog.WeeklyWordIndexPage']),
        PageChooserPanel('resources_index_page', ['resources.ResourceIndexPage']),
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
    
    class Meta:
        verbose_name_plural = _("Site Emails")

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


class SubscribeFormField(AbstractFormField):
    page = ParentalKey('SubscribeFormPage', on_delete=models.CASCADE, related_name='form_fields')

class SubscribeFormPage(AbstractEmailForm):
    template = 'blog/subscribe_form.html'
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
                landing_page_context['email'] = form.cleaned_data['email']

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
class SubscribeFormSettings(BaseSiteSetting):
    subscribe_form_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL)

    panels = [
        # note the page type declared within the pagechooserpanel
        PageChooserPanel('subscribe_form_page', ['blog.SubscribeFormPage']),
    ]