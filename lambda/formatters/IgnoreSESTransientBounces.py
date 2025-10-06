import json

from core import Formatter


class IgnoreSESTransientBounces(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        if sns_object['notificationType'] == 'Bounce' and sns_object['bounce']['bounceType'] == 'Transient':
            return {'ignore': True}

        return {
            'ignore': False,
            'formatted': False
        }