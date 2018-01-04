from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DRAGProj.urls')),
    path('Diversify/', include('DRAGProj.urls'))
]
