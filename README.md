# CloudWatch-Alarm-To-Slack

A AWS Lambda based service for sending Cloudwatch alarm to Slack. Uses CDK to provision stack (SNS, Lambda).

![Alt text](doc/overview.jpg "overview")

### Slack setup

1. Start by setting up an incoming webhook integration in your Slack workspace: https://my.slack.com/services/new/incoming-webhook/
2. Select a channel or create a new one
3. Click on *Add Incoming WebHooks integration*
4. You are redirected to a new page where you can see your *Webhook URL*. Copy the value; you will need it soon


### AWS setup

This project uses CDK for provisioning stack.

```bash
cp .env.example .env # then fill with new settings
cdk deploy
```

### CloudWatch alarm action setup
![Alt text](doc/set_cloudwatch_alarm_action.png "set action")


### More

The lambda function references from cloudwatch-alarm-to-slack-python


