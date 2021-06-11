import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from SMONU.settings import PAGINATION_SETTINGS
from blog.models import Article, Comments
from core.basic.basic_info import getAdminMenuList, getIndexInfoList, getCarouselDisplay, getColumnLists, \
    getContactInfoList, getHeaderAndFooterDict, getArticleListToDict, getArticleToDict
from core.basic_functions import DictMerge

from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # header_info 设置
    dict_info = getHeaderAndFooterDict(request)

    # carousel display List 轮播图设置
    carousel_display_List = getCarouselDisplay(request)
    dict_info = DictMerge(dict_info, carousel_display_List)

    # column_lists设置#
    column_lists_List = getColumnLists(request)
    dict_info = DictMerge(dict_info, column_lists_List)

    return render(request, "front/page/index.html", dict_info)


def error(request):
    # header_info 设置
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/404.html", dict_info)


def collections(request):
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/collections.html", dict_info)


def collections_list(request):
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/collections-list.html", dict_info)


def product(request):
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/product.html", dict_info)


def contact(request):
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/contact.html", dict_info)


def article(request, article_nub):
    dict_info = getHeaderAndFooterDict(request)
    title_url = article_nub
    article_s = None
    language = request.LANGUAGE_CODE.replace("-", "_")

    if request.session.get('article', {'nub': '', 'lang': ''})['nub'] == article_nub and \
            request.session.get('article', {'nub': '', 'lang': ''})['lang'] != language:
        article_s = Article.objects.get(title_id=request.session.get('article')['title_id'])
        article_ = getArticleToDict(request, article_s)
        del request.session['article']
        return HttpResponseRedirect('/' + request.LANGUAGE_CODE + '/article/' + article_.get('title_url'))
    else:
        title_url_find = []
        exec('title_url_find.append(Article.objects.filter(title_url_{0}=title_url))'.format(language))
        article_ = Article.objects.filter(title_id=article_nub)

        if article_.count() == 1:
            article_s = article_.get(title_id=article_nub)
        else:

            if title_url_find:

                exec('title_url_find.append(title_url_find[0].get(title_url_{0}=title_url))'.format(language))
                article_s = title_url_find[1]
                request.session['article'] = {
                    "nub": article_nub,
                    "title_id": article_s.title_id,
                    "lang": language,
                }
            else:
                print(article_s)
                return HttpResponseRedirect('/404.html')

        article_ = getArticleToDict(request, article_s)
        dict_info = DictMerge(dict_info, {
            'article': article_})
        comment = Comments.objects.filter(article_ID=article_s.title_id)
        dict_info = DictMerge(dict_info, {
            'comment': comment})
        dict_info = DictMerge(dict_info, {
            'language': request.LANGUAGE_CODE})
        return render(request, "front/page/article.html", dict_info)

@require_http_methods(["POST"])
def comment_add(request, article_nub):
    """
        暂时还缺乏中间件，或者函数功能，进行对于恶意数据的录入进行处理，加入黑名单要求。
        还缺功能是：进行不良信息文字限制，加入审核机制。进行调整和判断浏览者ip的是否存在恶意输入信息。
    """
    title_id = article_nub
    try:
        article_title = Article.objects.get(title_id=title_id)

        user = request.POST.get("name", '')
        email = request.POST.get("email", '')
        website = request.POST.get("website", '')
        textarea = request.POST.get("textarea", '')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        Comments.objects.create(article_ID=article_title.title_id, author=user, content=textarea, website=website,
                                email=email, IP=ip)
        # article_title.comment_count += 1
        article_title.save()
        ret = {"status": 1, 'url': '获取到POST信息！'}

        return HttpResponse(json.dumps(ret))
    except:
        ret = {"status": 0, 'url': '获取到信息失败！'}

        return HttpResponse(json.dumps(ret))


def article_info(request):
    dict_info = getHeaderAndFooterDict(request)

    return render(request, "front/page/article-info.html", dict_info)


def article_lists(request):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    # ar= Article.objects.all()
    # ar.get(id=0).thumbnail_image.url
    dict_info = getHeaderAndFooterDict(request)
    objects = getArticleListToDict(request)
    print(objects)
    org_nums = len(objects)
    print(objects)
    # Provide Paginator with the request object for complete querystring generation

    p = Paginator(objects, PAGINATION_SETTINGS['PAGE_NUMB'], request=request)

    article = p.page(page)
    print(article)
    dict_info = DictMerge(dict_info, {
        'article': article, "org_nums": org_nums})

    return render(request, "front/page/article-lists.html", dict_info)
    # return render(request, "front/page/article-lists.html", dict_info)
