from ckeditor_uploader.views import ImageUploadView
from django.conf.urls import url, static
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from SMONU import settings
from user.management import views

urlpatterns = [
    url(r'^$', views.index, name='management-admin/index.html'),
    url(r"^index.html", views.index, name='management-admin/index.html'),
    url(r"^login.html", views.Login.get, name='management-admin/login.html'),
    url(r'^login.html', views.Login.get, name='login.html'),
    url(r'^login', views.Login.post, name='login'),
    url(r"^information.html", views.PersonalInformation.get, name='management-admin/information.html'),
    url(r"^reset-password.html", views.ResetPassword.get, name='management-admin/reset-password.html'),
    url(r"^post-reset", views.ResetPassword.post, name='management-admin/post-reset'),
    url(r"^admin-manage.html", views.ManageAdmin.get, name='management-admin/admin-manage.html'),
    url(r"^post-admin", views.ManageAdmin.post, name='management-admin/post-admin'),
    url(r'^basicinfo/', include('user.basicinfo.urls')),
    url(r'^articlemanage/', include('user.articlemanage.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^ckeditor/', csrf_exempt(ImageUploadView.as_view())),  # 为富文本编辑器添加总路由

    #url(r'^upload/$', ImageUploadView.as_view(),name='ckeditor_upload'),

]

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_URL)
