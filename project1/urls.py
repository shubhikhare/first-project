from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^home/$', 'mine.views.home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
