# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from django.conf import settings
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from lizard_ui.urls import debugmode_urlpatterns

from controlnext import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^ui/', include('lizard_ui.urls')),
    # url(r'^map/', include('lizard_map.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        views.MainView.as_view(),
        name='controlnext-main'
    ),
    url(r'^prediction_data/$',
        views.PredictionDataView.as_view(),
        name='controlnext-prediction-data'
    )
)

if settings.DEBUG:
    urlpatterns += debugmode_urlpatterns()