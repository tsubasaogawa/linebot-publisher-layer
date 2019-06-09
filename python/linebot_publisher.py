import json
import os
import requests
import sys


class LineBotPublisher:
  """
  LINEBot Publisher.
  """
  # URL Endpoint
  ENDPOINT = 'https://api.line.me/v2/bot/message/push'

  # Access Token
  ACCESS_TOKEN = os.environ.get('LINE_BOT_ACCESS_TOKEN')

  def __init__(self, endpoint=ENDPOINT, access_token=ACCESS_TOKEN):
    """
    Constructor.

    Parameters
    ----------
    endpoint : string
        URL Endpoint to LINE Messaging API.
        Default is https://api.line.me/v2/bot/message/push

    access_token : string
        Access token of LINE Messaging API.
    """
    self._die_if_empty([endpoint, access_token])

    self.endpoint = endpoint
    self.access_token = access_token

  def post_text(self, to_id, text, notifies=True):
    """
    Post text to LINE Bot.

    Parameters
    ----------
    to_id : string
        userId, groupId or roomId
    text : string
        Message text
    notifies : bool
        Notify user(s) when it posts if True.
        Default is True.

    Returns
    -------
    response : Response
        It always returns 200.
    """
    self._die_if_empty([to_id, text])

    header = {
      "Content-Type": "application/json",
      "Authorization": "Bearer {}".format(self.access_token)
    }
    payload = {
      "to": to_id,
      "messages": [
        {
          "type": "text",
          "text": text
        }
      ],
      "notificationDisabled": not notifies
    }

    response = requests.post(
        self.endpoint,
        headers=header,
        data=json.dumps(payload)
    )

    return response

  def _die_if_empty(self, objects=[]):
    """
    Print message and exit program as an error if a given element is empty ('').

    Parameters
    ----------
    objects : list[string]
        List of string objects.
    """
    for obj in objects:
      if obj == '':
        print('{} is null.'.format(obj))
        sys.exit(1)

