import json

from core import Formatter


class SignIn(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        if sns_object['source'] == 'aws.signin':
            detail = sns_object['detail']
            lines = [
                'ROOT sign in',
                f'- {detail['eventName']}',
                f'- IP: {detail['sourceIPAddress']}',
            ]

            account = sns_object.get('account')
            if account:
                lines.append(f'- Account: {account}')

            login_result = detail.get('responseElements', {}).get('ConsoleLogin')
            if login_result:
                lines.append(f'- Login result: {login_result}')

            mfa_used = detail.get('additionalEventData', {}).get('MFAUsed')
            if mfa_used:
                lines.append(f'- MFA used: {mfa_used}')

            return {
                'formatted': True,
                'message': '\n'.join(lines),
                'ignore': False,
            }

        return {
            'ignore': False,
            'formatted': False
        }