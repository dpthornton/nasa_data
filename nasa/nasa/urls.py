"""nasa URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls


admin.site.site_title = 'Nasa Administration'

urlpatterns = [
    path('facilities/', include('facilities.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='NASA Facilities API', public=False))
]
