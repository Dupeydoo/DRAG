from django.contrib import admin
from django.urls import path, include

"""
Django module containing url routing for the DRAG application.

    Author:
        James
        
    Version:
        1.1.0
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DRAGProj.urls')),
    path('Diversify/', include('DRAGProj.urls'))
]
"""
urlpatterns (:obj:`list`): contains the controller patterns for different typed urls.
"""
