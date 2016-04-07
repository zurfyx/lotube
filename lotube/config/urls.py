from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bot/', include('bot.urls')),
    url(r'^api/v1/', include('config.urls_api', namespace='api')),
    url(r'^', include('config.urls_web', namespace='web')),
    url(r'^', RedirectView.as_view(url='videos'))
]
