from django.apps import AppConfig
from DRAGProj.dragcommon.appstart import AppStart

"""
The apps module. Exposes the app configuration for
DRAGProj to the settings file in the DRAG app.

    Author:
        James
        
    Version:
        1.0.0
"""


class DragprojConfig(AppConfig):
    """
    The DRAGProj config class. Exposes the name of the
    configuration to the website settings.

    Attributes:
        name (:obj:`str`): The name of the DRAGProj configuration.
    """
    name = 'DRAGProj'

    def ready(self):
        AppStart.clear = True
