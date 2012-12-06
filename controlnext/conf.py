# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
from __future__ import unicode_literals
import datetime

from django.conf import settings

from appconf import AppConf


class ControlNEXTConf(AppConf):
    """Configurable app settings."""
    JDBC_SOURCE_SLUG = "controlnext"
    JDBC_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    FEWSJDBC_CACHE_SECONDS = 15 * 60

    FILL_HISTORY = datetime.timedelta(days=31)
    FILL_PREDICT_FUTURE = datetime.timedelta(days=5)

    class Meta:
        prefix = 'controlnext'