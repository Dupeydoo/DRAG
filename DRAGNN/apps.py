from django.apps import AppConfig

"""
The DRAGNN apps module. Exposes the app configuration for
DRAGNN to the settings file in the DRAG app.

    Author:
        James

    Version:
        1.0.0
"""


class DragnnConfig(AppConfig):
    """
    The DRAGNN config class. Exposes the name of the
    configuration to the website settings.

    Attributes:
        name (:obj:`str`): The name of the DRAGNN configuration.
    """
    name = 'DRAGNN'
