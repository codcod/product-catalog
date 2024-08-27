# pylint: disable=C0114.C0115,C0116
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='index'),
]
