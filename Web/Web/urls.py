from django.contrib import admin
from django.urls import path
from main import views as m_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',m_view.index)
]
