from django.urls import path
from blog.views import BlogListView, HowListView, WordListView, VideoListView, SearchResultsList
app_name = "blog"

urlpatterns = [
    path('blogs/list/', BlogListView.as_view(), name='blog_list'),
    path('hows/list/', HowListView.as_view(), name='how_list'),
    path('word-of-the-week/list/', WordListView.as_view(), name='word_list'),
    path('videos/list/', VideoListView.as_view(), name='video_list'),

    path(
        route='search_results',
        view=SearchResultsList.as_view(),
        name='search_results'
    ),
    # path("<slug:slug>/", AuthorDetailView.as_view(), name="author_detail"),
]