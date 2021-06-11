from django.test import TestCase

# Create your tests here.
import os

import django

from django.contrib.auth.hashers import make_password

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMONU.settings")  # project_name 项目名称
django.setup()
# Create your tests here.
from user.models import RootProfile

macpw = make_password("SportsVideo123456", "importlib", 'pbkdf2_sha256')

RootProfile.objects.create(username="root", password=macpw)
"""
try:

    IndexInfo1 = IndexInfo.objects.create(page_info="IndexInfo",page_where="FirstOne")
    IndexInfo2 = IndexInfo.objects.create(page_info="IndexInfo",page_where="FirstTwo")
    IndexInfo3 = IndexInfo.objects.create(page_info="IndexInfo",page_where="FirstThere")

    IndexInfo4 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header1")
    IndexInfo5 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header2")
    IndexInfo6 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header3")
    IndexInfo7 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header4")
    IndexInfo8 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header5")
    IndexInfo9 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header6")
    IndexInfo10 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header7")
    IndexInfo11 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header8")
    IndexInfo12 = IndexInfo.objects.create(page_info="IndexInfo",page_where="Header9")

    IndexUrl1 = IndexUrl.objects.create(page_where="First1")
    IndexUrl2 = IndexUrl.objects.create(page_where="First2")
    IndexUrl3 = IndexUrl.objects.create(page_where="First3")
    IndexUrl4 = IndexUrl.objects.create(page_where="First4")
    smAdminMenu1_1 = SmAdminMenu.objects.create(parent_id=1, menu_mc="一", menu_order=1)
    smAdminMenu1_2 = SmAdminMenu.objects.create(parent_id=1, menu_mc="二", menu_order=2)
    smAdminMenu1_3 = SmAdminMenu.objects.create(parent_id=1, menu_mc="三", menu_order=3)
    smAdminMenu1_4 = SmAdminMenu.objects.create(parent_id=1, menu_mc="四", menu_order=4)
    smAdminMenu1_5 = SmAdminMenu.objects.create(parent_id=1, menu_mc="五", menu_order=5)
    smAdminMenu1_6 = SmAdminMenu.objects.create(parent_id=1, menu_mc="六", menu_order=6)
    smAdminMenu1_7 = SmAdminMenu.objects.create(parent_id=1, menu_mc="七", menu_order=7)
    
    smAdminMenu2_1 = SmAdminMenu.objects.create(parent_id=2, menu_mc="一", menu_order=1)
    smAdminMenu2_2 = SmAdminMenu.objects.create(parent_id=2, menu_mc="二", menu_order=2)
    smAdminMenu2_3 = SmAdminMenu.objects.create(parent_id=2, menu_mc="三", menu_order=3)
    smAdminMenu2_4 = SmAdminMenu.objects.create(parent_id=2, menu_mc="四", menu_order=4)
    smAdminMenu2_5 = SmAdminMenu.objects.create(parent_id=2, menu_mc="五", menu_order=5)
    smAdminMenu2_6 = SmAdminMenu.objects.create(parent_id=2, menu_mc="六", menu_order=6)
    smAdminMenu2_7 = SmAdminMenu.objects.create(parent_id=2, menu_mc="七", menu_order=7)
    
    
    smAdminMenu3_1 = SmAdminMenu.objects.create(parent_id=3, menu_mc="一", menu_order=1)
    smAdminMenu3_2 = SmAdminMenu.objects.create(parent_id=3, menu_mc="二", menu_order=2)
    smAdminMenu3_3 = SmAdminMenu.objects.create(parent_id=3, menu_mc="三", menu_order=3)
    smAdminMenu3_4 = SmAdminMenu.objects.create(parent_id=3, menu_mc="四", menu_order=4)
    smAdminMenu3_5 = SmAdminMenu.objects.create(parent_id=3, menu_mc="五", menu_order=5)
    smAdminMenu3_6 = SmAdminMenu.objects.create(parent_id=3, menu_mc="六", menu_order=6)
    smAdminMenu3_7 = SmAdminMenu.objects.create(parent_id=3, menu_mc="七", menu_order=7)
    
    smAdminMenu4_1 = SmAdminMenu.objects.create(parent_id=4, menu_mc="一", menu_order=1)
    smAdminMenu4_2 = SmAdminMenu.objects.create(parent_id=4, menu_mc="二", menu_order=2)
    smAdminMenu4_3 = SmAdminMenu.objects.create(parent_id=4, menu_mc="三", menu_order=3)
    smAdminMenu4_4 = SmAdminMenu.objects.create(parent_id=4, menu_mc="四", menu_order=4)
    smAdminMenu4_5 = SmAdminMenu.objects.create(parent_id=4, menu_mc="五", menu_order=5)
    smAdminMenu4_6 = SmAdminMenu.objects.create(parent_id=4, menu_mc="六", menu_order=6)
    smAdminMenu4_7 = SmAdminMenu.objects.create(parent_id=4, menu_mc="七", menu_order=7)
    
    smAdminMenu5_1 = SmAdminMenu.objects.create(parent_id=5, menu_mc="一", menu_order=1)
    smAdminMenu5_2 = SmAdminMenu.objects.create(parent_id=5, menu_mc="二", menu_order=2)
    smAdminMenu5_3 = SmAdminMenu.objects.create(parent_id=5, menu_mc="三", menu_order=3)
    smAdminMenu5_4 = SmAdminMenu.objects.create(parent_id=5, menu_mc="四", menu_order=4)
    smAdminMenu5_5 = SmAdminMenu.objects.create(parent_id=5, menu_mc="五", menu_order=5)
    smAdminMenu5_6 = SmAdminMenu.objects.create(parent_id=5, menu_mc="六", menu_order=6)
    smAdminMenu5_7 = SmAdminMenu.objects.create(parent_id=5, menu_mc="七", menu_order=7)
    
    smAdminMenu6_1 = SmAdminMenu.objects.create(parent_id=6, menu_mc="一", menu_order=1)
    smAdminMenu6_2 = SmAdminMenu.objects.create(parent_id=6, menu_mc="二", menu_order=2)
    smAdminMenu6_3 = SmAdminMenu.objects.create(parent_id=6, menu_mc="三", menu_order=3)
    smAdminMenu6_4 = SmAdminMenu.objects.create(parent_id=6, menu_mc="四", menu_order=4)
    smAdminMenu6_5 = SmAdminMenu.objects.create(parent_id=6, menu_mc="五", menu_order=5)
    smAdminMenu6_6 = SmAdminMenu.objects.create(parent_id=6, menu_mc="六", menu_order=6)
    smAdminMenu6_7 = SmAdminMenu.objects.create(parent_id=6, menu_mc="七", menu_order=7)
    
    
    smAdminMenu7_1 = SmAdminMenu.objects.create(parent_id=7, menu_mc="一", menu_order=1)
    smAdminMenu7_2 = SmAdminMenu.objects.create(parent_id=7, menu_mc="二", menu_order=2)
    smAdminMenu7_3 = SmAdminMenu.objects.create(parent_id=7, menu_mc="三", menu_order=3)
    smAdminMenu7_4 = SmAdminMenu.objects.create(parent_id=7, menu_mc="四", menu_order=4)
    smAdminMenu7_5 = SmAdminMenu.objects.create(parent_id=7, menu_mc="五", menu_order=5)
    smAdminMenu7_6 = SmAdminMenu.objects.create(parent_id=7, menu_mc="六", menu_order=6)
    smAdminMenu7_7 = SmAdminMenu.objects.create(parent_id=7, menu_mc="七", menu_order=7)
except:
    print("project_name已确立")


"""

from backstage.models import SmAdminMenu, IndexInfo, IndexUrl, NewsInfo, CarouselDisplay, ProductRecommendation, \
    CategoryRecommendation, FlowerImgUrl, ContactInfo, FooterListInfo

"""
IndexUrl2 = IndexUrl.objects.create(page_where="First5")
IndexUrl3 = IndexUrl.objects.create(page_where="First6")
IndexUrl4 = IndexUrl.objects.create(page_where="First7")

contactInfo1 = ContactInfo.objects.create(contact_nub=1, contact_name="一")
contactInfo2 = ContactInfo.objects.create(contact_nub=2, contact_name="二")
contactInfo3 = ContactInfo.objects.create(contact_nub=3, contact_name="三")
contactInfo4 = ContactInfo.objects.create(contact_nub=4, contact_name="四")
contactInfo5 = ContactInfo.objects.create(contact_nub=5, contact_name="五")
contactInfo6 = ContactInfo.objects.create(contact_nub=6, contact_name="六")
"""
IndexInfo6 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header3")
IndexInfo7 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header4")
IndexInfo8 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header5")
IndexInfo9 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header6")
IndexInfo10 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header7")
IndexInfo11 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header8")
IndexInfo12 = IndexInfo.objects.create(page_info="IndexInfo", page_where="Header9")