from django.contrib import admin
from django.urls import path, re_path
from menu.views import home, page_view

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^(?P<slug>.*)$', page_view, name='page'),
]