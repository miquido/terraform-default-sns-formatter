import json
import os
from FormattersFactory import FormattersFactory

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    formatters = os.getenv('FORMATTERS').split(',')
    formatters = list(map(lambda x: FormattersFactory.formatter(x), formatters))

    for formatter in formatters:
        try:
            formatted_message = formatter.format(event['message'])
            if formatted_message['ignore']:
                return {
                    'formatted': False,
                    'message': None,
                    'ignore': True,
                }
            if formatted_message['formatted']:
                return {
                    'formatted': True,
                    'message': formatted_message['message'],
                    'ignore': False,
                }
        except Exception as e:
            pass
    return {
        'formatted': False,
        'ignore': False,
    }

if __name__ == '__main__':
    handle = lambda_handler({'message': event}, None)

    print(json.dumps(handle, indent=2))
