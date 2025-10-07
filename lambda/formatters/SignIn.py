import json

from core import Formatter


class SignIn(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        if sns_object['source'] == 'aws.signin':
            return {
                'formatted': True,
                'message': f'ROOT sign in \n- {sns_object['detail']['eventName']}\n- IP: {sns_object['detail']['sourceIPAddress']}',
                'ignore': False,
            }

        return {
            'ignore': False,
            'formatted': False
        }