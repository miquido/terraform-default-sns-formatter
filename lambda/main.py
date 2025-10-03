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
    # event = '{"AlarmName":"example-dev-example-dev-test-cpu-credit-balance-low","AlarmDescription":"Average database CPU credit balance over last 10 minutes too low, expect a significant performance drop soon","AWSAccountId":"123456789","AlarmConfigurationUpdatedTimestamp":"2024-03-08T14:05:02.761+0000","NewStateValue":"ALARM","NewStateReason":"Threshold Crossed: 1 datapoint [0.0 (08/03/24 13:56:00)] was less than the threshold (20.0).","StateChangeTime":"2024-03-08T14:06:01.853+0000","Region":"US East (N. Virginia)","AlarmArn":"arn:aws:cloudwatch:us-east-1:123456789012:alarm:example-dev-example-dev-test-cpu-credit-balance-low","OldStateValue":"INSUFFICIENT_DATA","OKActions":["arn:aws:sns:us-east-1:123456789012:example-dev-example-dev-test-ok-rds-threshold-alerts20240308140459771500000003"],"AlarmActions":["arn:aws:sns:us-east-1:123456789012:example-dev-notifications"],"InsufficientDataActions":[],"Trigger":{"MetricName":"CPUCreditBalance","Namespace":"AWS/RDS","StatisticType":"Statistic","Statistic":"AVERAGE","Unit":null,"Dimensions":[{"value":"example-dev-test","name":"DBInstanceIdentifier"}],"Period":600,"EvaluationPeriods":1,"ComparisonOperator":"LessThanThreshold","Threshold":20.0,"TreatMissingData":"missing","EvaluateLowSampleCountPercentile":""}}'
    # event = '{"version":"0","id":"e26d4f75-6bbc-ecaf-d75f-046305d222d9","detail-type":"AWS API Call via CloudTrail","source":"aws.iam","account":"322231848625","time":"2025-10-03T08:41:04Z","region":"us-east-1","resources":[],"detail":{"eventVersion":"1.11","userIdentity":{"type":"AssumedRole","principalId":"AROAUWBUDZ2YWRNRVSP5J:marek.moscichowski@miquido.com","arn":"arn:aws:sts::322231848625:assumed-role/AdministratorAccess/marek.moscichowski@miquido.com","accountId":"322231848625","accessKeyId":"ASIAUWBUDZ2YXEDOUSTL","sessionContext":{"sessionIssuer":{"type":"Role","principalId":"AROAUWBUDZ2YWRNRVSP5J","arn":"arn:aws:iam::322231848625:role/AdministratorAccess","accountId":"322231848625","userName":"AdministratorAccess"},"attributes":{"creationDate":"2025-10-03T08:40:44Z","mfaAuthenticated":"true"}},"invokedBy":"resource-explorer-2.amazonaws.com"},"eventTime":"2025-10-03T08:41:04Z","eventSource":"iam.amazonaws.com","eventName":"CreateServiceLinkedRole","awsRegion":"us-east-1","sourceIPAddress":"resource-explorer-2.amazonaws.com","userAgent":"resource-explorer-2.amazonaws.com","requestParameters":{"aWSServiceName":"resource-explorer-2.amazonaws.com"},"responseElements":{"role":{"path":"/aws-service-role/resource-explorer-2.amazonaws.com/","roleName":"AWSServiceRoleForResourceExplorer","roleId":"AROAUWBUDZ2Y3CEZGVVPL","arn":"arn:aws:iam::322231848625:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer","createDate":"Oct 3, 2025, 8:41:04 AM","assumeRolePolicyDocument":"%7B%22Version%22%3A%20%222012-10-17%22%2C%20%22Statement%22%3A%20%5B%7B%22Action%22%3A%20%5B%22sts%3AAssumeRole%22%5D%2C%20%22Effect%22%3A%20%22Allow%22%2C%20%22Principal%22%3A%20%7B%22Service%22%3A%20%5B%22resource-explorer-2.amazonaws.com%22%5D%7D%7D%5D%7D"}},"requestID":"c957e852-48dd-4839-88ce-e1cd8de9dc97","eventID":"d91b36b6-016e-44c1-a0e0-47d7b4289926","readOnly":false,"eventType":"AwsApiCall","managementEvent":true,"recipientAccountId":"322231848625","eventCategory":"Management","sessionCredentialFromConsole":"true"}}'
    event = "{\"version\":\"0\",\"id\":\"35a187de-3aa4-6efe-a9a9-6377f6f7a43e\",\"detail-type\":\"AWS API Call via CloudTrail\",\"source\":\"aws.iam\",\"account\":\"246402711611\",\"time\":\"2025-10-03T13:18:38Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"eventVersion\":\"1.11\",\"userIdentity\":{\"type\":\"AssumedRole\",\"principalId\":\"AROATSXV7AA5R5KPXJ5NJ:marek.moscichowski@miquido.com\",\"arn\":\"arn:aws:sts::246402711611:assumed-role/AdministratorAccess/marek.moscichowski@miquido.com\",\"accountId\":\"246402711611\",\"accessKeyId\":\"ASIATSXV7AA54JZTHP4Q\",\"sessionContext\":{\"sessionIssuer\":{\"type\":\"Role\",\"principalId\":\"AROATSXV7AA5R5KPXJ5NJ\",\"arn\":\"arn:aws:iam::246402711611:role/AdministratorAccess\",\"accountId\":\"246402711611\",\"userName\":\"AdministratorAccess\"},\"attributes\":{\"creationDate\":\"2025-10-03T09:43:56Z\",\"mfaAuthenticated\":\"true\"}}},\"eventTime\":\"2025-10-03T13:18:38Z\",\"eventSource\":\"iam.amazonaws.com\",\"eventName\":\"AttachRolePolicy\",\"awsRegion\":\"us-east-1\",\"sourceIPAddress\":\"83.10.35.235\",\"userAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36\",\"requestParameters\":{\"roleName\":\"Playground-Test-notification-formatter-eu-central-1\",\"policyArn\":\"arn:aws:iam::aws:policy/AmazonAppFlowReadOnlyAccess\"},\"responseElements\":null,\"requestID\":\"2b2ac274-4dd5-44d1-9cbe-84c1e0f6a854\",\"eventID\":\"1d56d2a5-f24c-46c2-867f-4115d3261d82\",\"readOnly\":false,\"eventType\":\"AwsApiCall\",\"managementEvent\":true,\"recipientAccountId\":\"246402711611\",\"eventCategory\":\"Management\",\"tlsDetails\":{\"tlsVersion\":\"TLSv1.3\",\"cipherSuite\":\"TLS_AES_128_GCM_SHA256\",\"clientProvidedHostHeader\":\"iam.amazonaws.com\"},\"sessionCredentialFromConsole\":\"true\"}}"
    handle = lambda_handler({'message': event}, None)

    print(json.dumps(handle, indent=2))
