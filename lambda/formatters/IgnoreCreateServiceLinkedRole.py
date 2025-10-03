import json

from core import Formatter


class IgnoreCreateServiceLinkedRole(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        if sns_object['detail']['eventName'] == 'CreateServiceLinkedRole':
            return {'ignore': True}

        return {
            'ignore': False,
            'formatted': False
        }