import requests
import urllib
import jwt
from django.conf import settings

# Helper functions for publishing events, generating JWT tokens, and generating the Hub URL.

def publish_event(event_type, topic, targets):
    """
    Publishes an event to the Mercure Hub.
    event_type: The type of the event, can be any string
    topic: The topic the event will be sent to. Only subscribers who request this topic will get notified.
    targets: The targets that are eligible to get the event.
    """
    token = get_jwt_token([], targets)
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'type': event_type,
        'topic': topic,
        # Mercure expects this data field, even though we don't need it
        # for Intercooler updates.
        'data': '{}',
    }
    requests.post(
        settings.MERCURE_HUB_URL,
        data=data,
        headers=headers,
    )


def get_jwt_token(subscribe_targets, publish_targets):
    """
    Creates a Mercure JWT token with the subscribe and publish targets.
    The JWT token gets signed with a key shared with the Mercure Hub.
    """
    return jwt.encode(
        {
            'mercure': {
                'subscribe': subscribe_targets,
                'publish': publish_targets
            }
        },
        settings.MERCURE_JWT_KEY,
        algorithm='HS256'
    )


def get_hub_url(topics):
    """
    Returns the URL used to subscribe to the given topics in Mercure. The response
    will be an event stream.
    """
    params = [('topic', t) for t in topics]
    return settings.MERCURE_HUB_URL + '?' + urllib.parse.urlencode(params)