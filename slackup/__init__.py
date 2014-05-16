from os import environ
import os.path

from slacker import Slacker


SLACK_API_TOKEN = environ.get('SLACK_API_TOKEN')

if not SLACK_API_TOKEN:
    raise ValueError('Please specify an API token in your SLACK_API_TOKEN '
                     'environment variable.')

slack = Slacker(SLACK_API_TOKEN)


def upload(gross_channel_names, filename):
    channel_names = map(lambda n: n.lstrip('#'), gross_channel_names)

    channels = slack.channels.list()
    post_to_channels = []

    for channel in channels.body['channels']:
        if channel['name'] in channel_names:
            post_to_channels.append(channel)

    slack.files.upload(
        filename,
        filename=os.path.basename(filename),
        channels=','.join([c['id'] for c in post_to_channels]),
    )
