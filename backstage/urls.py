from django.urls import include
from django.conf.urls import url
from backstage.views import index, collections, collections_list, product, contact, error, article, article_lists, \
    article_info, comment_add

urlpatterns = [
    url(r'^$', index, name='index.html'),
    url(r'^index.html', index, name='index.html'),
    url(r'^404.html', error, name='404.html'),
    url(r'^collections.html', collections, name='collections.html'),
    url(r'^collections-list.html', collections_list, name='collections-list.html'),
    url(r'^product.html', product, name='product.html'),
    url(r'^contact.html', contact, name='contact.html'),
    url(r'^blog/(?P<article_nub>(.*).html)', article, name='article'),
    url(r'^comment_add/(?P<article_nub>(.*))', comment_add, name='comment_add'),

    #url(r'^article-info.html', article_info, name='article-info.html'),
    url(r'^blog', article_lists, name='blog'),
]