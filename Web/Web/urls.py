from django.contrib import admin
from django.urls import path, re_path
from main import views as m_view
from welcome import views as w_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',m_view.index),
    path('team/',m_view.team),
    path('404/',m_view.NotFound),
    path('welcome/', w_view.main)
    
]

handler404 = m_view.NotFound
