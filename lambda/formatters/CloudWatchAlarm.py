import json

from core import Formatter

class CloudWatchAlarm(Formatter):
    @staticmethod
    def format(record):
        sns_object = json.loads(record)
        return {
            'formatted': True,
            'message': f'- Alarm: {sns_object["AlarmName"]}\n- Account: {sns_object["AWSAccountId"]}\n- Description: {sns_object["AlarmDescription"]}',
            'ignore': False,
        }
