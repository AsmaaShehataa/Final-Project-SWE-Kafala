import debug_toolbar
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orphanage/',include('orphanage.urls')),
    path('',include('sponser.urls')),
    path('admin_kafala/',include('admin_kafala.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

