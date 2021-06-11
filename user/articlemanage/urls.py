from django.conf.urls import url

from user.articlemanage import views

urlpatterns = [
    # 栏目页面
    url(r"^management-article-lists.html", views.show_article_lists.get, name='management-article-lists.html'),
    url(r"^add-article.html", views.show_add_article.get, name='add-article.html'),
    url(r"^add-article", views.show_add_article.post, name='add-article'),

    url(r"^edit-article.html", views.show_edit_article.get, name='edit-article.html'),
    url(r"^edit-basic-article", views.show_edit_article.basic_post, name='edit-basic-article'),
    url(r"^edit-article", views.show_edit_article.post, name='edit-article'),

]