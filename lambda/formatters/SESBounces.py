import json

from core import Formatter


class SESBounces(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        try:
            diagnostic = f"\n- Diagnostic:{sns_object['bounce']['bouncedRecipients'][0]['diagnosticCode']}"
        except KeyError as e:
            diagnostic = ""
        if sns_object['notificationType'] == 'Bounce':
            return {
                'formatted': True,
                'message': f'SES Bounce:\n- Mail: {sns_object['mail']['destination']}\n- Type: {sns_object['bounce']['bounceType']}{diagnostic}',
                'ignore': False,
            }
        if sns_object['notificationType'] == 'Complaint':
            return {
                'formatted': True,
                'message': f'SES Complaint:\n- Mail: {sns_object['mail']['destination']}\n- Type: {sns_object['complaint']['complaintFeedbackType']}{diagnostic}',
                'ignore': False,
            }
        return {
            'formatted': False,
            'ignore': False,
        }