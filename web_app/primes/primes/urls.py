from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from .views import PrimeView, PrimeAsyncView


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^prime/$', PrimeView.as_view(), ),
    url(r'^prime-async/$', PrimeAsyncView.as_view(), ),

    url(r'^admin/', include(admin.site.urls)),
)


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
