from django.contrib import admin
from django.urls import path

from code_search_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index_view, name='index'),
    path('search', views.search_view, name='search'),
    path('code/<str:code_hash>', views.code_document_view, name='code_document'),
]