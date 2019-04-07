import json
import os
import requests


class LineBotPublisher:
  ENDPOINT = os.environ['LINE_BOT_ENDPOINT'] # 'https://api.line.me/v2/bot/message/reply'
  ACCESS_TOKEN = os.environ['LINE_BOT_ACCESS_TOKEN']

  def post_text(self, to_id, text):
    header = {
      "Content-Type": "application/json",
      "Authorization": "Bearer {0}".format(self.ACCESS_TOKEN)
    }
    payload = {
      "to": to_id,
      "messages": [
        {
          "type": "text",
          "text": text
        }
      ]
    }
    requests.post(self.ENDPOINT, headers=header, data=json.dumps(payload))

    return True

