from django.contrib import admin
from DRAGProj.models.preset import Preset
from DRAGProj.models.anonymoususer import AnonymousUser

"""
The DRAGProj admin module. Handles registration of
models in the admin section of the website.

    Author:
        James
        
    Version:
        1.0.0
"""

# Register models with the admin controls.
# This allows the website superuser to manipulate
# database information from /admin.
admin.site.register(Preset)
admin.site.register(AnonymousUser)
