from django.urls import path
from blog.views import BlogListView, HowListView, WordListView, VideoListView, SearchResultsList
from blog.models import blogLike, howLike, wordLike
app_name = "blog"

urlpatterns = [
    path('blogs/list/', BlogListView.as_view(), name='blog_list'),
    path('hows/list/', HowListView.as_view(), name='how_list'),
    path('word-of-the-week/list/', WordListView.as_view(), name='word_list'),
    path('videos/list/', VideoListView.as_view(), name='video_list'),
    path('blog/like/<int:pk>', blogLike, name='blog_like'),
    path('how/like/<int:pk>', howLike, name='how_like'),
    path('word/like/<int:pk>', wordLike, name='word_like'),

    path(
        route='search_results',
        view=SearchResultsList.as_view(),
        name='search_results'
    ),
    # path("<slug:slug>/", AuthorDetailView.as_view(), name="author_detail"),
]