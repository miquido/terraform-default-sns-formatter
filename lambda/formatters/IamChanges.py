import json

from core import Formatter


class IamChanges(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        if sns_object['detail']['eventSource'] == 'iam.amazonaws.com':

            request = f'{''.join(f'  - {k}: {v}\n' for k, v in sns_object['detail']['requestParameters'].items() if k != 'policyDocument')}'

            return {
                'formatted': True,
                'message': f'IAM Changes: \n- principal: {sns_object['detail']['userIdentity']['principalId']}\n- Event: {sns_object['detail']['eventName']}\n- Request: \n{request}',
                'ignore': False,
            }

        return {
            'ignore': False,
            'formatted': False
        }