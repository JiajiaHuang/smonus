import time

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from backstage.models import SmAdminMenu, IndexInfo, CarouselDisplay, NewsInfo, ContactInfo, ColumnListsInfo
from core.session.ManageSession import getheader_info


@login_required
def header_index(request):
    """
    # 管理首页
    :param request:h=success&i=v1
    :return:
    """
    h = request.GET.get("h", "")
    i = request.GET.get("i", "")
    info = {}
    if h == "success" and i != "":
        info["s"] = True
        info["e"] = False
        info["info"] = "修改成功！"

    elif h == "error" and i != "":
        info["s"] = False
        info["e"] = True
        info["info"] = "修改失敗！"
    else:
        info["s"] = False
        info["e"] = False

    header_info = getheader_info(request)
    adminMenuList = {}
    for parent_id in range(1, 8):
        smAdminMenu = SmAdminMenu.objects.filter(parent_id=parent_id).order_by('menu_order')
        adminMenuList["menu_" + str(parent_id)] = smAdminMenu
    print(adminMenuList)
    URL_Info = IndexInfo.objects.all()  #
    Carousel_Info = CarouselDisplay.objects.all().order_by('carousel_nub')  #
    News_Info = NewsInfo.objects.all()  #
    Contact_Info = ContactInfo.objects.all()  #

    return render(request, "backstage/userauth/pagefile/page/header-index.html",
                  {"header_info": header_info, "adminMenuList": adminMenuList, "info": info, "URL_Info": URL_Info,
                   "Carousel_Info": Carousel_Info, "News_Info": News_Info, "Contact_Info": Contact_Info})


@login_required
def footer_index(request):
    """
    # 管理首页
    :param request:h=success&i=v1
    :return:
    """
    h = request.GET.get("h", "")
    i = request.GET.get("i", "")
    info = {}
    if h == "success" and i != "":
        info["s"] = True
        info["e"] = False
        info["info"] = "修改成功！"

    elif h == "error" and i != "":
        info["s"] = False
        info["e"] = True
        info["info"] = "修改失敗！"
    else:
        info["s"] = False
        info["e"] = False

    header_info = getheader_info(request)
    adminMenuList = {}
    for parent_id in range(1, 8):
        smAdminMenu = SmAdminMenu.objects.filter(parent_id=parent_id).order_by('menu_order')
        adminMenuList["menu_" + str(parent_id)] = smAdminMenu
    print(adminMenuList)
    column_lists = ColumnListsInfo.objects.all().order_by('column_lists_nub')   #

    return render(request, "backstage/userauth/pagefile/page/foot-index.html",
                  {"header_info": header_info, "adminMenuList": adminMenuList, "info": info,
                   "column_lists": column_lists})


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def add_menu(request):
    """

    :param request:
    :return:
    """
    menu = request.GET.get("menu")
    menu_name = request.POST.get("menu_name", "")
    menu_url = request.POST.get("menu_url", "")
    menu_ft = request.POST.get("menu_ft", "")
    menu_jt = request.POST.get("menu_jt", "")
    menu_yw = request.POST.get("menu_yw", "")
    menu_fw = request.POST.get("menu_fw", "")
    menu_xby = request.POST.get("menu_xby", "")
    menu_pty = request.POST.get("menu_pty", "")
    print("POST不打開", menu, menu_name, menu_url)
    sm_nub = SmAdminMenu.objects.filter(parent_id=menu).count()
    SmAdminMenu.objects.create(parent_id=menu, menu_mc=menu_name, menu_order=sm_nub + 1, url=menu_url,
                               nenu_names_zh_hant=menu_ft, nenu_names_zh_hans=menu_jt, nenu_names_en=menu_yw,
                               nenu_names_fr=menu_fw, nenu_names_pt=menu_xby, nenu_names_es=menu_pty)

    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
def del_menu(request):
    """

    :param request:
    :return:
    """
    menu = request.GET.get("menu")
    menu_order = request.GET.get("menu_order")
    menu_count = SmAdminMenu.objects.filter(parent_id=menu).count()
    SmAdminMenu.objects.filter(parent_id=menu, menu_order=menu_order).delete()
    print(menu_order, menu_count)
    for nub in range(int(menu_order), menu_count + 1):
        print(menu_order, menu_count)
        SmAdminMenu.objects.filter(parent_id=menu, menu_order=nub).update(menu_order=nub - 1)

    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
class change_menu(View):
    def get(request):
        header_info = getheader_info(request)
        menu = request.GET.get("menu")
        menu_order = request.GET.get("menu_order")
        smAdminMenu = SmAdminMenu.objects.get(parent_id=menu, menu_order=menu_order)

        print(smAdminMenu)
        return render(request, "backstage/userauth/pagefile/base/headerindex/addform/page/change-menu.html",
                      {"header_info": header_info, "smAdminMenu": smAdminMenu})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        menu = request.GET.get("menu")
        menu_order = request.GET.get("menu_order")
        menu_name = request.POST.get("menu_name", "")
        menu_url = request.POST.get("menu_url", "")
        menu_ft = request.POST.get("menu_ft", "")
        menu_jt = request.POST.get("menu_jt", "")
        menu_yw = request.POST.get("menu_yw", "")
        menu_fw = request.POST.get("menu_fw", "")
        menu_xby = request.POST.get("menu_xby", "")
        menu_pty = request.POST.get("menu_pty", "")
        print("POST不打開", menu, menu_order, menu_name, menu_url)
        SmAdminMenu.objects.filter(parent_id=menu, menu_order=menu_order).update(menu_mc=menu_name,
                                                                                 url=menu_url,
                                                                                 nenu_names_zh_hant=menu_ft,
                                                                                 nenu_names_zh_hans=menu_jt,
                                                                                 nenu_names_en=menu_yw,
                                                                                 nenu_names_fr=menu_fw,
                                                                                 nenu_names_pt=menu_xby,
                                                                                 nenu_names_es=menu_pty)

        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
def change_menu_add(request):
    menu = request.GET.get("menu")
    menu_order = request.GET.get("menu_order")
    sm_nub = SmAdminMenu.objects.filter(parent_id=menu).count()
    if int(menu_order) >= sm_nub:
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html?h=error&i=v1")
    sm_one = SmAdminMenu.objects.get(parent_id=int(menu), menu_order=int(menu_order))
    sm_two = SmAdminMenu.objects.get(parent_id=int(menu), menu_order=int(menu_order) + 1)
    sm_one.menu_order = int(menu_order) + 1
    sm_two.menu_order = int(menu_order)
    sm_one.save()
    sm_two.save()

    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html?h=success&i=v1")


@login_required
def change_menu_dir(request):
    menu = request.GET.get("menu")
    menu_order = request.GET.get("menu_order")
    sm_nub = 1
    if int(menu_order) <= sm_nub:
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html?h=error&i=v1")
    print(int(menu), int(menu_order))
    sm_one = SmAdminMenu.objects.get(parent_id=int(menu), menu_order=int(menu_order) - 1)
    sm_two = SmAdminMenu.objects.get(parent_id=int(menu), menu_order=int(menu_order))
    sm_one.menu_order = int(menu_order) + 1
    sm_two.menu_order = int(menu_order)
    sm_one.save()
    sm_two.save()

    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html?h=success&i=v1")


@login_required
class change_url_info(View):
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")
        index_info = IndexInfo.objects.get(id=menu_order)

        print(index_info)
        return render(request, "backstage/userauth/pagefile/base/headerindex/addform/page/change-urlinfo.html",
                      {"header_info": header_info, "index_info": index_info})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        menu = request.GET.get("menu")
        page_info = request.POST.get("page_info", "")
        page_where = request.POST.get("page_where", "")
        page_url = request.POST.get("page_url", "")
        page_name_zh_hant = request.POST.get("page_name_zh_hant", "")
        page_name_zh_hans = request.POST.get("page_name_zh_hans", "")
        page_name_en = request.POST.get("page_name_en", "")
        page_name_fr = request.POST.get("page_name_fr", "")
        page_name_es = request.POST.get("page_name_es", "")
        page_name_pt = request.POST.get("page_name_pt", "")
        print("POST不打開", page_where, menu, page_info, page_url)
        IndexInfo.objects.filter(id=menu).update(page_info=page_info, page_where=page_where, page_url=page_url,
                                                 page_name_zh_hant=page_name_zh_hant,
                                                 page_name_zh_hans=page_name_zh_hans, page_name_en=page_name_en,
                                                 page_name_fr=page_name_fr, page_name_es=page_name_es,
                                                 page_name_pt=page_name_pt)
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
class add_news_list(View):
    def get(request):
        header_info = getheader_info(request)

        return render(request, "backstage/userauth/pagefile/base/headerindex/addform/page/newslist/add-news-list.html",
                      {"header_info": header_info})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        news_name = request.POST.get("news_name", "")
        news_url = request.POST.get("news_url", "")
        news_info_zh_hant = request.POST.get("news_info_zh_hant", "")
        news_info_zh_hans = request.POST.get("news_info_zh_hans", "")
        news_info_en = request.POST.get("news_info_en", "")
        news_info_fr = request.POST.get("news_info_fr", "")
        news_info_es = request.POST.get("news_info_es", "")
        news_info_pt = request.POST.get("news_info_pt", "")
        NewsInfo.objects.create(news_name=news_name, news_url=news_url, news_info_zh_hant=news_info_zh_hant,
                                news_info_zh_hans=news_info_zh_hans, news_info_en=news_info_en,
                                news_info_fr=news_info_fr, news_info_es=news_info_es, news_info_pt=news_info_pt)
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
class change_news_list(View):
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")

        news_info = NewsInfo.objects.get(id=menu_order)

        print(news_info)
        return render(request,
                      "backstage/userauth/pagefile/base/headerindex/addform/page/newslist/change-news-list.html",
                      {"header_info": header_info, "news_info": news_info})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        menu = request.GET.get("menu")
        news_name = request.POST.get("news_name", "")
        news_url = request.POST.get("news_url", "")
        news_info_zh_hant = request.POST.get("news_info_zh_hant", "")
        news_info_zh_hans = request.POST.get("news_info_zh_hans", "")
        news_info_en = request.POST.get("news_info_en", "")
        news_info_fr = request.POST.get("news_info_fr", "")
        news_info_es = request.POST.get("news_info_es", "")
        news_info_pt = request.POST.get("news_info_pt", "")
        NewsInfo.objects.filter(id=menu).update(news_name=news_name, news_url=news_url,
                                                news_info_zh_hant=news_info_zh_hant,
                                                news_info_zh_hans=news_info_zh_hans, news_info_en=news_info_en,
                                                news_info_fr=news_info_fr, news_info_es=news_info_es,
                                                news_info_pt=news_info_pt)
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
def del_news_list(request):
    menu = request.GET.get("menu_order", "")
    NewsInfo.objects.filter(id=menu).delete()
    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


@login_required
class add_homecarousel(View):
    def get(request):
        header_info = getheader_info(request)
        count = CarouselDisplay.objects.all().count() + 1
        return render(request,
                      "backstage/userauth/pagefile/base/headerindex/addform/page/homecarousel/add-homecarousel.html",
                      {"header_info": header_info, 'count': count})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        carousel_nub = CarouselDisplay.objects.all().count() + 1
        carousel_img = request.FILES['carousel_img']
        carousel_url = request.POST.get("carousel_url", "")

        carousel_info_zh_hant = request.POST.get("carousel_info_zh_hant", "")
        carousel_info_zh_hans = request.POST.get("carousel_info_zh_hans", "")
        carousel_info_en = request.POST.get("carousel_info_en", "")
        carousel_info_fr = request.POST.get("carousel_info_fr", "")
        carousel_info_es = request.POST.get("carousel_info_es", "")
        carousel_info_pt = request.POST.get("carousel_info_pt", "")
        # add_homecarousel
        carousel_display = CarouselDisplay.objects.create(carousel_nub=carousel_nub, carousel_url=carousel_url,
                                                          carousel_info_zh_hant=carousel_info_zh_hant,
                                                          carousel_info_zh_hans=carousel_info_zh_hans,
                                                          carousel_info_en=carousel_info_en,
                                                          carousel_info_fr=carousel_info_fr,
                                                          carousel_info_es=carousel_info_es,
                                                          carousel_info_pt=carousel_info_pt)
        carousel_display.carousel_img.save('card' + str(time.time())[0:9] + str(time.time())[5:0] + ".jpg",
                                           carousel_img, save=True)

        carousel_display.save()
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html#homecarousel")


@login_required
class change_homecarousel(View):
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")

        carousel_display = CarouselDisplay.objects.get(id=menu_order)

        return render(request,
                      "backstage/userauth/pagefile/base/headerindex/addform/page/homecarousel/change-homecarousel.html",
                      {"header_info": header_info, "carousel_display": carousel_display})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        menu_order = request.GET.get("menu_order")
        carousel_url = request.POST.get("carousel_url", "")
        try:
            carousel_img = request.FILES['carousel_img']
        except:
            carousel_img = None
        carousel_info_zh_hant = request.POST.get("carousel_info_zh_hant", "")
        carousel_info_zh_hans = request.POST.get("carousel_info_zh_hans", "")
        carousel_info_en = request.POST.get("carousel_info_en", "")
        carousel_info_fr = request.POST.get("carousel_info_fr", "")
        carousel_info_es = request.POST.get("carousel_info_es", "")
        carousel_info_pt = request.POST.get("carousel_info_pt", "")
        carousel_display = CarouselDisplay.objects.get(carousel_nub=menu_order)
        carousel_display.carousel_url = carousel_url
        carousel_display.carousel_info_zh_hant = carousel_info_zh_hant
        carousel_display.carousel_info_zh_hans = carousel_info_zh_hans
        carousel_display.carousel_info_en = carousel_info_en
        carousel_display.carousel_info_fr = carousel_info_fr
        carousel_display.carousel_info_es = carousel_info_es
        carousel_display.carousel_info_pt = carousel_info_pt

        if carousel_img is not None:
            carousel_display.carousel_img.save('card' + str(time.time())[0:9] + str(time.time())[5:0] + ".jpg",
                                               carousel_img, save=True)
        carousel_display.save()

        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html#homecarousel")


@login_required
def del_homecarousel(request):
    menu_order = request.GET.get("menu_order")
    menu_count = CarouselDisplay.objects.all().count()
    CarouselDisplay.objects.get(carousel_nub=menu_order).delete()

    print(menu_order, menu_count)
    for nub in range(int(menu_order), menu_count + 1):
        print(nub, menu_order, menu_count)
        CarouselDisplay.objects.filter(carousel_nub=nub + 1).update(carousel_nub=nub)

    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html#homecarousel")


@login_required
def up_homecarousel(request):
    menu_order = request.GET.get("menu_order")
    menu_count = CarouselDisplay.objects.all().count()
    if 1 < int(menu_order) <= menu_count:
        c1 = CarouselDisplay.objects.get(carousel_nub=menu_order)
        c2 = CarouselDisplay.objects.get(carousel_nub=int(menu_order) - 1)
        c1.carousel_nub = int(menu_order) - 1
        c2.carousel_nub = int(menu_order)
        c1.save()
        c2.save()
    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html#homecarousel")


@login_required
def down_homecarousel(request):
    menu_order = request.GET.get("menu_order")
    menu_count = CarouselDisplay.objects.all().count()
    if 1 <= int(menu_order) < menu_count:
        c1 = CarouselDisplay.objects.get(carousel_nub=menu_order)
        c2 = CarouselDisplay.objects.get(carousel_nub=int(menu_order) + 1)
        c1.carousel_nub = int(menu_order) + 1
        c2.carousel_nub = int(menu_order)
        c1.save()
        c2.save()
    return HttpResponseRedirect("/management-admin/basicinfo/header_index.html#homecarousel")


@login_required
class change_enter_info(View):
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")
        index_info = ContactInfo.objects.get(id=menu_order)

        print(index_info)
        return render(request, "backstage/userauth/pagefile/base/headerindex/addform/page/change-enterinfo.html",
                      {"header_info": header_info, "index_info": index_info})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        menu = request.GET.get("menu")
        contact_nub = request.POST.get("contact_nub", "")
        contact_name = request.POST.get("contact_name", "")
        contact_url = request.POST.get("contact_url", "")
        contact_info_zh_hant = request.POST.get("contact_info_zh_hant", "")
        contact_info_zh_hans = request.POST.get("contact_info_zh_hans", "")
        contact_info_en = request.POST.get("contact_info_en", "")
        contact_info_fr = request.POST.get("contact_info_fr", "")
        contact_info_es = request.POST.get("contact_info_es", "")
        contact_info_pt = request.POST.get("contact_info_pt", "")
        print("POST不打開", contact_nub, menu, contact_name, contact_url)
        ContactInfo.objects.filter(id=menu).update(contact_nub=contact_nub, contact_name=contact_name,
                                                   contact_url=contact_url,
                                                   contact_info_zh_hant=contact_info_zh_hant,
                                                   contact_info_zh_hans=contact_info_zh_hans,
                                                   contact_info_en=contact_info_en,
                                                   contact_info_fr=contact_info_fr, contact_info_es=contact_info_es,
                                                   contact_info_pt=contact_info_pt)
        return HttpResponseRedirect("/management-admin/basicinfo/header_index.html")


# ************************************                                      *******************************************#
# carousel_list

class add_carousel_list(View):
    @login_required
    def get(request):
        header_info = getheader_info(request)
        count = ColumnListsInfo.objects.all().count() + 1

        return render(request,
                      "backstage/userauth/pagefile/base/footerindex/addform/page/homecarousel/add-homecarousel.html",
                      {"header_info": header_info,'count':count})

    @login_required
    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        column_lists_nub = ColumnListsInfo.objects.all().count() + 1
        column_url = request.POST.get("column_url", "")

        column_lists_img = request.FILES['column_lists_img']

        column_lists_title_zh_hant = request.POST.get("column_lists_title_zh_hant", "")
        column_lists_title_zh_hans = request.POST.get("column_lists_title_zh_hans", "")
        column_lists_title_en = request.POST.get("column_lists_title_en", "")
        column_lists_title_fr = request.POST.get("column_lists_title_fr", "")
        column_lists_title_es = request.POST.get("column_lists_title_es", "")
        column_lists_title_pt = request.POST.get("column_lists_title_pt", "")

        column_lists_subtitle_zh_hant = request.POST.get("column_lists_subtitle_zh_hant", "")
        column_lists_subtitle_zh_hans = request.POST.get("column_lists_subtitle_zh_hans", "")
        column_lists_subtitle_en = request.POST.get("column_lists_subtitle_en", "")
        column_lists_subtitle_fr = request.POST.get("column_lists_subtitle_fr", "")
        column_lists_subtitle_es = request.POST.get("column_lists_subtitle_es", "")
        column_lists_subtitle_pt = request.POST.get("column_lists_subtitle_pt", "")

        column_lists_alt_zh_hant = request.POST.get("column_lists_alt_zh_hant", "")
        column_lists_alt_zh_hans = request.POST.get("column_lists_alt_zh_hans", "")
        column_lists_alt_en = request.POST.get("column_lists_alt_en", "")
        column_lists_alt_fr = request.POST.get("column_lists_alt_fr", "")
        column_lists_alt_es = request.POST.get("column_lists_alt_es", "")
        column_lists_alt_pt = request.POST.get("column_lists_alt_pt", "")

        column_lists = ColumnListsInfo.objects.create(column_lists_nub=column_lists_nub, column_url=column_url,
                                                      column_lists_title_zh_hant=column_lists_title_zh_hant,
                                                      column_lists_title_zh_hans=column_lists_title_zh_hans,
                                                      column_lists_title_en=column_lists_title_en,
                                                      column_lists_title_fr=column_lists_title_fr,
                                                      column_lists_title_es=column_lists_title_es,
                                                      column_lists_title_pt=column_lists_title_pt,
                                                      column_lists_subtitle_zh_hant=column_lists_subtitle_zh_hant,
                                                      column_lists_subtitle_zh_hans=column_lists_subtitle_zh_hans,
                                                      column_lists_subtitle_en=column_lists_subtitle_en,
                                                      column_lists_subtitle_fr=column_lists_subtitle_fr,
                                                      column_lists_subtitle_es=column_lists_subtitle_es,
                                                      column_lists_subtitle_pt=column_lists_subtitle_pt,
                                                      column_lists_alt_zh_hant=column_lists_alt_zh_hant,
                                                      column_lists_alt_zh_hans=column_lists_alt_zh_hans,
                                                      column_lists_alt_en=column_lists_alt_en,
                                                      column_lists_alt_fr=column_lists_alt_fr,
                                                      column_lists_alt_es=column_lists_alt_es,
                                                      column_lists_alt_pt=column_lists_alt_pt,
                                                      )
        column_lists.column_lists_img.save('card' + str(time.time())[0:9] + str(time.time())[5:0] + ".jpg",
                                           column_lists_img, save=True)
        column_lists.save()
        return HttpResponseRedirect("/management-admin/basicinfo/footer_index.html")


class change_carousel_lists(View):
    @login_required
    def get(request):
        header_info = getheader_info(request)
        menu_order = request.GET.get("menu_order")

        carousel_display = ColumnListsInfo.objects.get(id=menu_order)

        return render(request,
                      "backstage/userauth/pagefile/base/footerindex/addform/page/homecarousel/change-homecarousel.html",
                      {"header_info": header_info, "carousel_display": carousel_display})

    @login_required
    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        column_lists_nub = request.GET.get("menu_order", "")
        column_url = request.POST.get("column_url", "")
        try:
            column_lists_img = request.FILES['column_lists_img']
        except:
            column_lists_img = None

        print(column_lists_nub)

        column_lists_title_zh_hant = request.POST.get("column_lists_title_zh_hant", "")
        column_lists_title_zh_hans = request.POST.get("column_lists_title_zh_hans", "")
        column_lists_title_zh_en = request.POST.get("column_lists_title_en", "")
        column_lists_title_fr = request.POST.get("column_lists_title_fr", "")
        column_lists_title_es = request.POST.get("column_lists_title_es", "")
        column_lists_title_pt = request.POST.get("column_lists_title_pt", "")

        column_lists_subtitle_zh_hant = request.POST.get("column_lists_subtitle_zh_hant", "")
        column_lists_subtitle_zh_hans = request.POST.get("column_lists_subtitle_zh_hans", "")
        column_lists_subtitle_zh_en = request.POST.get("column_lists_subtitle_en", "")
        column_lists_subtitle_zh_fr = request.POST.get("column_lists_subtitle_fr", "")
        column_lists_subtitle_zh_es = request.POST.get("column_lists_subtitle_es", "")
        column_lists_subtitle_zh_pt = request.POST.get("column_lists_subtitle_pt", "")

        column_lists_alt_zh_hant = request.POST.get("column_lists_alt_zh_hant", "")
        column_lists_alt_zh_hans = request.POST.get("column_lists_alt_zh_hans", "")
        column_lists_alt_zh_en = request.POST.get("column_lists_alt_en", "")
        column_lists_alt_zh_fr = request.POST.get("column_lists_alt_fr", "")
        column_lists_alt_zh_es = request.POST.get("column_lists_alt_es", "")
        column_lists_alt_zh_pt = request.POST.get("column_lists_alt_pt", "")
        column_lists = ColumnListsInfo.objects.get(column_lists_nub=column_lists_nub)
        column_lists.column_url = column_url

        column_lists.column_lists_title_zh_hant = column_lists_title_zh_hant
        column_lists.column_lists_title_zh_hans = column_lists_title_zh_hans
        column_lists.column_lists_title_en = column_lists_title_zh_en
        column_lists.column_lists_title_fr = column_lists_title_fr
        column_lists.column_lists_title_es = column_lists_title_es
        column_lists.column_lists_title_pt = column_lists_title_pt

        column_lists.column_lists_subtitle_zh_hant = column_lists_subtitle_zh_hant
        column_lists.column_lists_subtitle_zh_hans = column_lists_subtitle_zh_hans
        column_lists.column_lists_subtitle_en = column_lists_subtitle_zh_en
        column_lists.column_lists_subtitle_fr = column_lists_subtitle_zh_fr
        column_lists.column_lists_subtitle_es = column_lists_subtitle_zh_es
        column_lists.column_lists_subtitle_pt = column_lists_subtitle_zh_pt

        column_lists.column_lists_alt_zh_hant = column_lists_alt_zh_hant
        column_lists.column_lists_alt_zh_hans = column_lists_alt_zh_hans
        column_lists.column_lists_alt_en = column_lists_alt_zh_en
        column_lists.column_lists_alt_fr = column_lists_alt_zh_fr
        column_lists.column_lists_alt_es = column_lists_alt_zh_es
        column_lists.column_lists_alt_pt = column_lists_alt_zh_pt
        print(column_lists_img)
        if column_lists_img is not None:
            column_lists.column_lists_img.save('card' + str(time.time())[0:9] + str(time.time())[5:0] + ".jpg",
                                               column_lists_img, save=True)
        column_lists.save()

        return HttpResponseRedirect("/management-admin/basicinfo/footer_index.html")


@login_required
def del_carousel_lists(request):
    menu_order = request.GET.get("menu_order")
    menu_count = CarouselDisplay.objects.all().count()
    ColumnListsInfo.objects.get(column_lists_nub=menu_order).delete()

    print(menu_order, menu_count)
    for nub in range(int(menu_order), menu_count + 1):
        print(nub, menu_order, menu_count)
        ColumnListsInfo.objects.filter(column_lists_nub=nub + 1).update(column_lists_nub=nub)

    return HttpResponseRedirect("/management-admin/basicinfo/footer_index.html")


@login_required
def up_carousel_lists(request):
    menu_order = request.GET.get("menu_order")
    menu_count = ColumnListsInfo.objects.all().count()
    if 1 < int(menu_order) <= menu_count:
        c1 = ColumnListsInfo.objects.get(column_lists_nub=menu_order)
        c2 = ColumnListsInfo.objects.get(column_lists_nub=int(menu_order) - 1)
        c1.column_lists_nub = int(menu_order) - 1
        c2.column_lists_nub = int(menu_order)
        c1.save()
        c2.save()
    return HttpResponseRedirect("/management-admin/basicinfo/footer_index.html")


@login_required
def down_carousel_lists(request):
    menu_order = request.GET.get("menu_order")
    menu_count = ColumnListsInfo.objects.all().count()
    if 1 <= int(menu_order) < menu_count:
        c1 = ColumnListsInfo.objects.get(column_lists_nub=menu_order)
        c2 = ColumnListsInfo.objects.get(column_lists_nub=int(menu_order) + 1)
        c1.column_lists_nub = int(menu_order) + 1
        c2.column_lists_nub = int(menu_order)
        c1.save()
        c2.save()
    return HttpResponseRedirect("/management-admin/basicinfo/footer_index.html")

# *********************************                                      ***********************************************#
