from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from .routers import router

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'api/v1/', include(router.urls)),
    url('', TemplateView.as_view(template_name='index.html'))
]
