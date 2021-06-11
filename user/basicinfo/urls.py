from django.conf.urls import url
from user.basicinfo import views


urlpatterns = [
    # 栏目页面
    url(r"^header_index.html", views.header_index, name='header_index.html'),
    url(r"^footer_index.html", views.footer_index, name='footer_index.html'),
    #
    url(r"^change_menu.html", views.change_menu.get, name='change_menu.html'),
    url(r"^post_change_menu.html", views.change_menu.post, name='post_change_menu.html'),

    url(r"^del_menu.html", views.del_menu, name='del_menu.html'),
    url(r"^add_menu.html", views.add_menu, name='add_menu.html'),

    url(r"^change_menu_add.html", views.change_menu_add, name='change_menu_add.html'),
    url(r"^change_menu_dir.html", views.change_menu_dir, name='change_menu_dir.html'),

    url(r"^change_url_info.html", views.change_url_info.get, name='change_url_info.html'),
    url(r"^post_change_url_info.html", views.change_url_info.post, name='post_change_url_info.html'),

    url(r"^change_enter_info.html", views.change_enter_info.get, name='change_enter_info.html'),
    url(r"^post_change_enter_info.html", views.change_enter_info.post, name='post_change_enter_info.html'),

    url(r"^add_news_list.html", views.add_news_list.get, name='add_news_list.html'),
    url(r"^post_add_news_list.html", views.add_news_list.post, name='post_add_news_list.html'),
    url(r"^change_news_list.html", views.change_news_list.get, name='change_news_list.html'),
    url(r"^post_change_news_list.html", views.change_news_list.post, name='post_change_news_list.html'),
    url(r"^del_news_list.html", views.del_news_list, name='del_news_list.html'),


    # 首页轮播图片与文案


    url(r"^add-homecarousel.html", views.add_homecarousel.get, name='add-homecarousel.html'),
    url(r"^post-add-homecarousel.html", views.add_homecarousel.post, name='post-add-homecarousel.html'),

    url(r"^del-homecarousel.html", views.del_homecarousel, name='del-homecarousel.html'),
    url(r"^up-homecarousel.html", views.up_homecarousel, name='up-homecarousel.html'),
    url(r"^down-homecarousel.html", views.down_homecarousel, name='down-homecarousel.html'),

    url(r"^change-homecarousel.html", views.change_homecarousel.get, name='change-homecarousel.html'),
    url(r"^post-change-homecarousel.html", views.change_homecarousel.post, name='post-change-homecarousel.html'),

    #栏目图片与文案

    url(r"^add-carousel-lists.html", views.add_carousel_list.get, name='add-carousel-lists.html'),
    url(r"^post-add-carousel-lists.html", views.add_carousel_list.post, name='post-add-carousel-lists.html'),

    url(r"^del-carousel-lists.html", views.del_carousel_lists, name='del-column-lists.html'),
    url(r"^up-carousel-lists.html", views.up_carousel_lists, name='up-column-lists.html'),
    url(r"^down-carousel-lists.html", views.down_carousel_lists, name='down-column-lists.html'),

    url(r"^change-column-lists.html", views.change_carousel_lists.get, name='change-column-lists.html'),
    url(r"^post-change-column-lists.html", views.change_carousel_lists.post, name='post-change-column-lists.html'),

]