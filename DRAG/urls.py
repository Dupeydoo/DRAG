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
    path('', include('DRAGNN.urls'))
]
"""
urlpatterns (:obj:`list`): contains the controller patterns for different typed urls.
"""

# Error page handlers when released in production.
handler404 = 'DRAGProj.views.page_not_found_error'
"""
handler404 (:obj:`str`): The path to the 404 page to display in production.
"""
handler500 = 'DRAGProj.views.server_error'
"""
handler500 (:obj:`str`): The path to the 500 page to display in production.
"""
