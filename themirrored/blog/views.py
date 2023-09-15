from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.

from blog.models import BlogPage, Author, HowPage, WeeklyWordPage, VideoPage


class BlogListView(TemplateView):
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = BlogPage.objects.all()
        return context
    
class HowListView(TemplateView):
    template_name = "blog/how_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hows"] = HowPage.objects.all()
        return context
    
class WordListView(TemplateView):
    template_name = "blog/word_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["words"] = WeeklyWordPage.objects.all()
        return context
    
class VideoListView(TemplateView):
    template_name = "blog/video_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = VideoPage.objects.all()
        return context
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/author_detail.html'