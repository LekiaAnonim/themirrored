from django.conf import settings
from blog.models import Category, BlogPage
from home.models import HomePage

def base_data(request):
    data = {}
    blogs = BlogPage.objects.live().all()
    home_page = HomePage.objects.live().all().first()
    categories = Category.objects.live().all()
    data["blogs"] = blogs
    data["categories"] = categories
    data['home_page'] = home_page

    return data