from django.contrib import admin
from DRAGProj.models.preset import Preset
from DRAGProj.models.anonymoususer import AnonymousUser

admin.site.register(Preset)
admin.site.register(AnonymousUser)
