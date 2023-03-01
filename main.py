import requests
import json

def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))

webhook = "https://hooks.slack.com/services/XXXXX/XXXXX/XXXXXXXXXX"
payload = {"text": "Test Message from Python"}
send_slack_message(payload, webhook)
