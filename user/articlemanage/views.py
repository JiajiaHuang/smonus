import time

from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from SMONU.settings import LANGUAGES
from blog.models import Article
from core.basic_functions import set_flow
from core.fields import MultilingualField
from core.session.ManageSession import getheader_info, get_basic_info


class show_article_lists(View):
    @login_required
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")

        article_list = Article.objects.all()

        return render(request,
                      "backstage/userauth/pagefile/page/article-management.html",
                      {"header_info": header_info, "article_list": article_list})


@login_required
class show_add_article(View):
    @login_required
    def get(request):
        header_info = getheader_info(request)
        basic_info = get_basic_info(request)
        menu_order = request.GET.get("menu_order")

        article_list = Article.objects.all().order_by('-id')[:1]
        print(article_list)
        if article_list.count() != 0:
            print(article_list[0].id)
            title_id = set_flow(article_list[0].id + 1)
        else:
            title_id = set_flow(1)

        return render(request,
                      "backstage/userauth/pagefile/base/articlemanagement/addform/page/add-article.html",
                      {"header_info": header_info, "basic_info": basic_info, "article_list": article_list,
                       "title_id": title_id})

    @login_required
    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        basic_info = get_basic_info(request)

        title_id = request.GET.get("title_id", "")

        account_ID = request.POST.get("account_ID", "")
        owner_ID = request.POST.get("owner_ID", "")
        source = request.POST.get("source", "")
        allow_comments = request.POST.get("allow_comments", "")
        is_show = request.POST.get("is_show", "")

        process_state = request.POST.get("process_state", "")
        channel_ID = 1
        channel_name = request.POST.get("channel_name", "")
        privacy_level = request.POST.get("privacy_level", "")
        tags = request.POST.get("tags", "")
        # request.session["title_id"] = title_id

        # request.session.get('tags', None)
        if allow_comments == "on":
            allow_comments = True
        else:
            allow_comments = False

        if is_show == "on":
            is_show = True
        else:
            is_show = False

        if process_state == "on":
            process_state = True
        else:
            process_state = False

        if privacy_level == "on":
            privacy_level = True
        else:
            privacy_level = False
        try:
            thumbnail_image = request.FILES['thumbnail_image']
            is_image = True
        except:
            thumbnail_image = None
            is_image = False

        article = Article.objects.filter(title_id=title_id)

        if article.count() != 0:

            article_list = Article.objects.all().order_by('-id')[:1]
            if article_list.count() != 0:
                title_id = set_flow(article_list[0].id + 1)
            else:
                title_id = set_flow(1)
        new_article = Article.objects.create(title_id=title_id, account_ID=basic_info['user_name'], owner_ID=owner_ID,
                                             source=source, is_image=is_image, is_deleted=False,
                                             allow_comments=allow_comments, is_show=is_show,
                                             process_state=process_state,
                                             channel_ID=channel_ID, channel_name=channel_name,
                                             privacy_level=privacy_level, tags=tags)
        if is_image:
            new_article.thumbnail_image.save('title' + str(time.time()) + ".jpg", thumbnail_image, save=True)
            new_article.save()
        return HttpResponseRedirect('/management-admin/articlemanage/edit-article.html?title_id=%s' % title_id)


@login_required
class show_edit_article(View):
    @login_required
    def get(request):
        header_info = getheader_info(request)
        basic_info = get_basic_info(request)
        title_id = request.GET.get("title_id")
        language = request.GET.get("language", 'zh_hans')

        article = Article.objects.get(title_id=title_id)
        languages_list = []
        for lang in LANGUAGES:
            languages_list.append(lang[0].replace("-", "_"), )
        if language not in languages_list:
            return HttpResponseRedirect('/management-admin/articlemanage/management-article-lists.html')
        languages = []
        for lang in LANGUAGES:
            if lang[0].replace("-", "_") == language:
                languages.append((lang[0].replace("-", "_"), lang[1], True))
            else:
                languages.append((lang[0].replace("-", "_"), lang[1], False))
        more_text = ['title', 'subtitle', 'keyword', 'description_key', 'content', 'title_url']
        multilingual_text = {}
        for mx in more_text:
            exec("multilingual_text['{0}'] = article.{0}_{1}".format(mx, language))

        multilingual_text['language'] = language

        return render(request,
                      "backstage/userauth/pagefile/base/articlemanagement/editform/page/edit-article.html",
                      {"header_info": header_info, "basic_info": basic_info, "article": article,
                       "title_id": title_id, 'languages': languages, 'multilingual_text': multilingual_text})

    @login_required
    @csrf_exempt
    @require_http_methods(["POST"])
    def basic_post(request):
        basic_info = get_basic_info(request)

        title_id = request.GET.get("title_id", "")

        account_ID = request.POST.get("account_ID", "")
        owner_ID = request.POST.get("owner_ID", "")
        source = request.POST.get("source", "")
        allow_comments = request.POST.get("allow_comments", "")
        is_show = request.POST.get("is_show", "")

        process_state = request.POST.get("process_state", "")
        channel_ID = 1
        channel_name = request.POST.get("channel_name", "")
        privacy_level = request.POST.get("privacy_level", "")
        tags = request.POST.get("tags", "")


        if allow_comments == "on":
            allow_comments = True
        else:
            allow_comments = False

        if is_show == "on":
            is_show = True
        else:
            is_show = False

        if process_state == "on":
            process_state = True
        else:
            process_state = False

        if privacy_level == "on":
            privacy_level = True
        else:
            privacy_level = False
        try:
            thumbnail_image = request.FILES['thumbnail_image']
            is_image = True
        except:
            thumbnail_image = None
            is_image = False

        article = Article.objects.filter(title_id=title_id)

        if article.count() == 1:
            article.update(title_id=title_id, account_ID=basic_info['user_name'],
                           owner_ID=owner_ID,
                           source=source, is_image=is_image, is_deleted=False,
                           allow_comments=allow_comments, is_show=is_show,
                           process_state=process_state,
                           channel_ID=channel_ID, channel_name=channel_name,
                           privacy_level=privacy_level, tags=tags)
            new_article = article.get(title_id=title_id)
            if is_image:
                new_article.thumbnail_image.save('title' + str(time.time()) + ".jpg", thumbnail_image, save=True)
                new_article.save()
            return HttpResponseRedirect('/management-admin/articlemanage/edit-article.html?title_id=%s' % title_id)

        else:
            return HttpResponseRedirect('/management-admin/articlemanage/management-article-lists.html')

    @login_required
    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        title_id = request.GET.get("title_id", "")

        language = request.GET.get("language", "")
        title = request.POST.get("title", "")
        subtitle = request.POST.get("subtitle", "")
        keyword = request.POST.get("keyword", "")
        title_url = request.POST.get("title_url", "")

        description_key = request.POST.get("description_key", "")
        content = request.POST.get("content", "")

        title_url_find = exec('Article.objects.filter(title_url_{0}=title_url)'.format(language))
        if title_url_find:
            print(True)
        article = Article.objects.filter(title_id=title_id)

        title_url_find = []
        exec('title_url_find.append(Article.objects.filter(title_url_{0}=title_url))'.format(language))
        print(title_url_find[0],title_url)
        print(not title_url_find[0] , title_url != "")
        if not(not title_url_find[0] or title_url != ""):
            title_url = "{0}.html".format(title_id)
        print(LANGUAGES)
        languages = []
        for lang in LANGUAGES:
            languages.append(lang[0].replace("-", "_"), )
        if language not in languages:
            return HttpResponseRedirect('/management-admin/articlemanage/management-article-lists.html')
        if article.count() == 1:
            new_article = article.get(title_id=title_id)
            exec('new_article.title_{0} = title'.format(language))
            exec('new_article.subtitle_{0} = subtitle'.format(language))
            exec('new_article.keyword_{0} = keyword'.format(language))
            exec('new_article.description_key_{0} = description_key'.format(language))
            exec('new_article.content_{0} = content'.format(language))
            exec('new_article.title_url_{0} = title_url'.format(language))

            new_article.save()
            # new_article.content.val(language, content)
            # new_article.save()
            return HttpResponseRedirect(
                '/management-admin/articlemanage/edit-article.html?title_id=%s&language=%s#article-form' % (
                    title_id, language))
        else:
            return HttpResponseRedirect('/management-admin/articlemanage/management-article-lists.html')
