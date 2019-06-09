# linebot-publisher-layer

The simplest message post module to LINE Bot.
It works on AWS Lambda Layer.

## Example

```python
# import module
import linebot_publisher

# create instance
publisher = linebot_publisher.LineBotPublisher()

# post
publisher.post_text(
  os.environ.get('LINE_BOT_TO_ID'),
  'test message'
)
```

![Post Image](https://raw.githubusercontent.com/tsubasaogawa/linebot-publisher-layer/images/line_image.png)

## Methods

### post_text(to_id, text, notifies=True)

Post a LINE message with `text` to `to_id`. `to_id` is <userId>, <roomId> or <groupId>.
It does not notify user(s) when posts if `notifies` is False.

It returns `Response` object with status code 200.
