"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from blog.feeds import AllPostsRssFeed
#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views

import xadmin



urlpatterns = [
#    path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    # 记得在顶部引入 AllPostsRssFeed
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^search/', include('haystack.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^users/', include('users.urls')),
    # 将 auth 应用中的 urls 模块包含进来
    url(r'^users/', include('django.contrib.auth.urls')),
    # 别忘记在顶部引入 views 模块
    url(r'^$', views.index_re, name='index_re')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)