# linebot-publisher-layer

The simplest message post module to LINE Bot.
It works on AWS Lambda Layer.

## Example

Set `LINE_BOT_ACCESS_TOKEN` environment variable in advance.

```python
# import module
import linebot_publisher

# create instance
publisher = linebot_publisher.LineBotPublisher()

# post
publisher.post_text(
  'xxx',  # LINEBOT_TO_ID
  'test message'
)
```

### Post image

![Post Image](https://raw.githubusercontent.com/tsubasaogawa/linebot-publisher-layer/images/line_image.png)

## Required environment variables

### LINEBOT_ACCESS_TOKEN

An access token

## Methods

### LineBotPublisher(access_token=ACCESS_TOKEN, endpoint=ENDPOINT)

Constructor.
If `access_token` is not given, module obtains from environment variable named `LINE_BOT_ACCESS_TOKEN`.
`endpoint` is defined as 'https://api.line.me/v2/bot/message/push' in module.

### post_text(to_id, text, notifies=True)

Post a LINE message with `text` to `to_id`. `to_id` is <userId>, <roomId> or <groupId>.
It does not notify user(s) when posts if `notifies` is False.

It returns `Response` object with status code 200.

