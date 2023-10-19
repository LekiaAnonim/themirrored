from django.contrib import admin

# # Register your models here.
# Register your models here.
from .models import SiteSocial,SiteContact,RequestFormSettings, SiteLogo,ImportantPages, Category, IpModel, Video, VideoIndexPage, BlogPage, BlogIndexPage, BlogTagIndexPage, HowPage, HowIndexPage, WeeklyWordPage, WeeklyWordIndexPage
@admin.register(BlogPage)
class BlogAdmin(admin.ModelAdmin):
    fields = ('post_title','date_created', 'date_updated', 'post_image', 'body', 'allow_comments', 'post_category', 'article_of_the_week', 'tags', 'read_time', 'views', 'likes')
    list_display = ('post_title','date_created', 'date_updated', 'post_image', 'body', 'allow_comments', 'post_category', 'article_of_the_week', 'tags', 'read_time')
    list_filter = ('post_title', 'date_created',)
    search_fields = ('post_title', 'date_created',)
