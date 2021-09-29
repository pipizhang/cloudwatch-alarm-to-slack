#-*- coding: utf-8 -*-
import os

from aws_cdk import (
    core as cdk,
    aws_sns as sns,
    aws_sns_subscriptions as sns_subscriptions,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_python as lambda_python
)


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # sns topic
        topic = self.create_sns_topic()
        # lambda layer
        self.lambda_layers = self.create_lambda_layers()
        # service
        self.create_service(topic)

    def create_sns_topic(self):
        """Create SNS topic for CloudWatch alarm"""

        topic = sns.Topic(self,
                id = 'alarm_to_slack_sns_topic',
                topic_name = 'alarm-events',
                fifo = False
                )

        return topic

    def create_lambda_layers(self):
        """Create lambda layers"""

        layers = {}

        layers['python_requests'] = _lambda.LayerVersion(self,
            id='python_requests_module',
            code=_lambda.Code.asset('../lambda_layers/python/requests.zip'),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
            license='MIT',
            layer_version_name='PythonRequestsModule',
            description='Provides python requests module')

        return layers

    def create_service(self, topic):
        """Create alarm-to-slack service"""

        svc_lambda = _lambda.Function(self,
            id = 'alarm_to_slack_lambda',
            function_name = 'alarm-to-slack',
            handler = 'lambda_function.lambda_handler',
            runtime = _lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.asset('../lambda'),
            description= 'Sending CloudWatch alarm to Slack',
            memory_size = 128,
            timeout = cdk.Duration.seconds(30),
            layers = [self.lambda_layers['python_requests']],
            environment = {
                'SLACK_WEBHOOK_URL': os.getenv('SLACK_WEBHOOK_URL')
            })

        topic.add_subscription(sns_subscriptions.LambdaSubscription(svc_lambda))


