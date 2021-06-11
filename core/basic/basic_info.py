from django.forms import model_to_dict

from backstage.models import SmAdminMenu, IndexInfo, CarouselDisplay, ColumnListsInfo, ContactInfo
from blog.models import Article
from core.basic_functions import DictMerge
from core.fields import MultilingualField


def getAdminMenuList(request):
    """

    :param request:
    :return:
    """
    adminMenuList = {}
    for parent_id in range(1, 8):
        sm_menu_list = []

        smAdminMenu = SmAdminMenu.objects.filter(parent_id=parent_id).order_by('menu_order')
        for s_list in range(smAdminMenu.count()):
            # sm_menu = serializers.serialize('json', [smAdminMenu[s_list], ])
            # print(sm_menu)

            di = model_to_dict(smAdminMenu[s_list])
            s_dict = {'url': di['url'],
                      'nenu_names': di[MultilingualField.localized_field_name(
                          'nenu_names', request.session['_language'])]}

            sm_menu_list.append(s_dict)

        adminMenuList["menu_" + str(parent_id)] = sm_menu_list
    return {'adminMenuList': adminMenuList}


def getIndexInfoList(request):
    index_info_List = dict()
    index_info = IndexInfo.objects.all()
    for i_list in index_info:
        di = model_to_dict(i_list)
        index_info_List[i_list.page_where] = dict()
        index_info_List[i_list.page_where]["page_info"] = i_list.page_info
        index_info_List[i_list.page_where]["page_url"] = i_list.page_url
        index_info_List[i_list.page_where]["page_name"] = di[MultilingualField.localized_field_name(
            'page_name', request.session['_language'])]
    print(index_info_List)
    return {"index_info": index_info_List}


def getCarouselDisplay(request):
    carousel_display = CarouselDisplay.objects.all().order_by('carousel_nub')
    carousel_display_List = ['' for x in range(carousel_display.count())]

    print(carousel_display_List, carousel_display.count())
    for c_list in range(carousel_display.count()):
        print(carousel_display[c_list])
        ci = model_to_dict(carousel_display[c_list])
        c_dict = {'carousel_img': ci['carousel_img'],
                  'carousel_url': ci['carousel_url'],
                  'carousel_info': ci[MultilingualField.localized_field_name(
                      'carousel_info', request.session['_language'])]}

        carousel_display_List[int(ci['carousel_nub']) - 1] = c_dict
    return {"carousel_display": carousel_display_List}


def getColumnLists(request):
    column_lists = ColumnListsInfo.objects.all().order_by('column_lists_nub')
    column_lists_List = ['' for x in range(column_lists.count())]
    print(column_lists_List, column_lists.count())
    for c_list in range(column_lists.count()):
        print(column_lists[c_list])
        ci = model_to_dict(column_lists[c_list])
        c_dict = {'column_url': ci['column_url'],
                  'column_lists_img': ci['column_lists_img'],
                  'column_lists_title': ci[MultilingualField.localized_field_name(
                      'column_lists_title', request.session['_language'])],
                  'column_lists_subtitle': ci[MultilingualField.localized_field_name(
                      'column_lists_subtitle', request.session['_language'])],
                  'column_lists_alt': ci[MultilingualField.localized_field_name(
                      'column_lists_alt', request.session['_language'])],
                  }

        column_lists_List[int(ci['column_lists_nub']) - 1] = c_dict
    return {"column_lists_List": column_lists_List}


def getContactInfoList(request):
    contact_info_List = dict()
    contact_info = ContactInfo.objects.all()

    for c_contact_info in contact_info:
        ci = model_to_dict(c_contact_info)
        print(c_contact_info.contact_nub)

        contact_info_List[c_contact_info.contact_nub] = dict()
        contact_info_List[c_contact_info.contact_nub]["contact_name"] = c_contact_info.contact_name
        contact_info_List[c_contact_info.contact_nub]["contact_url"] = c_contact_info.contact_url
        contact_info_List[c_contact_info.contact_nub]["contact_info"] = ci[MultilingualField.localized_field_name(
            'contact_info', request.session['_language'])]
    print(contact_info_List)
    return {"contact_info_List": contact_info_List}


def getHeaderAndFooterDict(request):
    header_info = {
        'countryinfo': request.session['ip2country'],
        'weather': request.session['weather']
    }
    dict_info = dict()
    dict_info = DictMerge(dict_info, {'header_info': header_info})

    # admin Menu List 设置
    adminMenuList = getAdminMenuList(request)
    dict_info = DictMerge(dict_info, adminMenuList)

    # index_info_List 设置
    index_info_List = getIndexInfoList(request)
    dict_info = DictMerge(dict_info, index_info_List)
    # contact_info设置
    contact_info_List = getContactInfoList(request)
    dict_info = DictMerge(dict_info, contact_info_List)
    return dict_info


def getArticleListToDict(request):
    article_lists = Article.objects.all().order_by('-updated')
    article_lists_List = []
    for c_list in range(article_lists.count()):
        ci = model_to_dict(article_lists[c_list])
        article = article_lists.get(title_id=ci['title_id'])
        article_dict = dict()
        try:
            tags_list = eval(ci['tags'])

        except:
            tags_list = [{"value": ""}]

        if not ci['is_deleted'] and ci['process_state']:
            article_dict = {
                "title": ci[MultilingualField.localized_field_name(
                    'title', request.session['_language'])],
                "channel_name": ci['channel_name'],
                "title_url": ci[MultilingualField.localized_field_name(
                    'title_url', request.session['_language'])],
                "updated": ci['created'],
                "subtitle": ci[MultilingualField.localized_field_name(
                    'subtitle', request.session['_language'])],
                "thumbnail_image": '/' + ci['thumbnail_image'].url,
                # "is_deleted": ci['is_deleted'],
                "is_image": ci['is_image'],
                "is_show": ci['is_show'],
                "tags": tags_list
            }
            article_lists_List.append(article_dict)

    return article_lists_List


def getArticleToDict(request, article_):
    ci = model_to_dict(article_)
    try:
        tags_list = eval(ci['tags'])

    except:
        tags_list = [{"value": ""}]
    article_dict = None
    if not ci['is_deleted'] and ci['process_state']:
        article_dict = {
            "title_id":ci['title_id'],
            "title": ci[MultilingualField.localized_field_name('title', request.session['_language'])],
            "channel_name": ci['channel_name'],
            "title_url": ci[MultilingualField.localized_field_name('title_url', request.session['_language'])],
            "updated": ci['created'],
            "source": ci['source'],
            "comment_count": ci['comment_count'],
            "content": ci[MultilingualField.localized_field_name('content', request.session['_language'])],
            "subtitle": ci[MultilingualField.localized_field_name('subtitle', request.session['_language'])],
            "keyword": ci[MultilingualField.localized_field_name('keyword', request.session['_language'])],
            "description_key": ci[MultilingualField.localized_field_name('description_key', request.session['_language'])],
            "thumbnail_image": '/' + ci['thumbnail_image'].url,
            # "is_deleted": ci['is_deleted'],
            "is_image": ci['is_image'],
            "is_show": ci['is_show'],
            "tags": tags_list
        }
    return article_dict
