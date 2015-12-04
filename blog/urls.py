from django.conf.urls import patterns, url
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
import django.conf.urls
import django.views.defaults

urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
        ),
    # Individual posts
    url(r'^blog/(?P<pub_date__year>\d{4})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        ),
        name='post'
        ),
    #robots.txt
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/", content_type="text/plain")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





