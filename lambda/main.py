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
    event = '{"version":"0","id":"4218fa2a-d3e1-bd32-c1dc-98c2337e1d6f","detail-type":"AWS API Call via CloudTrail","source":"aws.iam","account":"873370528721","time":"2025-10-06T06:33:34Z","region":"us-east-1","resources":[],"detail":{"eventVersion":"1.11","userIdentity":{"type":"AssumedRole","principalId":"AROA4WWHQVPI4FPWERTQQ:aws-go-sdk-1759732395432419000","arn":"arn:aws:sts::873370528721:assumed-role/AdministratorAccess/aws-go-sdk-1759732395432419000","accountId":"873370528721","accessKeyId":"ASIA4WWHQVPIYANRLEYF","sessionContext":{"sessionIssuer":{"type":"Role","principalId":"AROA4WWHQVPI4FPWERTQQ","arn":"arn:aws:iam::873370528721:role/AdministratorAccess","accountId":"873370528721","userName":"AdministratorAccess"},"attributes":{"creationDate":"2025-10-06T06:33:16Z","mfaAuthenticated":"true"}}},"eventTime":"2025-10-06T06:33:34Z","eventSource":"iam.amazonaws.com","eventName":"PutRolePolicy","awsRegion":"us-east-1","sourceIPAddress":"45.144.121.18","userAgent":"APN/1.0 HashiCorp/1.0 Terraform/1.5.7 (+https://www.terraform.io) terraform-provider-aws/6.14.1 (+https://registry.terraform.io/providers/hashicorp/aws) aws-sdk-go-v2/1.39.0 ua/2.1 os/macos lang/go#1.24.6 md/GOOS#darwin md/GOARCH#amd64 api/iam#1.47.5 m/i","requestParameters":{"roleName":"passbolt-Prod-notification-us-east-1","policyName":"passbolt-Prod-notification-policy","policyDocument":"{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Action\\":[\\"logs:PutLogEvents\\",\\"logs:CreateLogStream\\"],\\"Effect\\":\\"Allow\\",\\"Resource\\":\\"arn:aws:logs:us-east-1:873370528721:log-group:/aws/lambda/passbolt-Prod-notification*\\"},{\\"Action\\":\\"ssm:GetParameter\\",\\"Effect\\":\\"Allow\\",\\"Resource\\":\\"arn:aws:ssm:us-east-1:873370528721:parameter/passbolt/Prod/webhooks/0\\"},{\\"Action\\":\\"lambda:InvokeFunction\\",\\"Effect\\":\\"Allow\\",\\"Resource\\":\\"arn:aws:lambda:us-east-1:873370528721:function:passbolt-Prod-notification-formatter\\"}]}"},"responseElements":null,"requestID":"6efb8a1b-5128-4368-ac80-a74e1488b155","eventID":"e8b1cc4d-32a6-4291-ba2e-dc27fa475f3b","readOnly":false,"eventType":"AwsApiCall","managementEvent":true,"recipientAccountId":"873370528721","eventCategory":"Management","tlsDetails":{"tlsVersion":"TLSv1.3","cipherSuite":"TLS_AES_128_GCM_SHA256","clientProvidedHostHeader":"iam.amazonaws.com"}}}'
    handle = lambda_handler({'message': event}, None)

    print(json.dumps(handle, indent=2))
