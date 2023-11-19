

from django.contrib import admin
from django.urls import path , include
import debug_toolbar
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

admin.site.site_header = _('اداراة المشاريع')
admin.site.site_title = ('إداراة المشاريع')

urlpatterns = [
    path('', include('projects.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('accounts.urls'))

]
