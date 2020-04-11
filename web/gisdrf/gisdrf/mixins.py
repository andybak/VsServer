from django.conf import settings
from . import mercure

# View mixin used for views that will subscribe to real-time events

class MercureMixin(object):
    """
    This view mixin will add a Set-Cookie header to the response. This cookie will
    include authorization information for the Mercure Hub in the form of a JWT token.
    The view needs to implement the subscribe and publish targets.
    """

    # Views that need to subscribe to events on the client should override this
    # attribute with the targets to subcribe to.
    mercure_subscribe_targets = []

    # Views that need to publish events from the client should override this
    # attribute with the targets to publish to.
    mercure_publish_targets = []

    # Views that need to subscribe to events should override this attribute
    # with the topics to subscribe to.
    mercure_hub_topics = []

    def get_mercure_subscribe_targets(self):
        """
        If the view needs to dynamically determine subscribe targets, it can
        override this method.
        """
        return self.mercure_subscribe_targets

    def get_mercure_publish_targets(self):
        """
        If the view needs to dynamically determine publish targets, it can
        override this method.
        """
        return self.mercure_publish_targets

    def get_mercure_hub_topics(self):
        """
        If the view needs to dynamically determine topics, it can
        override this method.
        """
        return self.mercure_hub_topics

    def dispatch(self, request, *args, **kwargs):
        """
        If Mercure is enabled, we will set a cookie in the response with
        a JWT token used for authentication/authorization with the Mercure Hub.
        Connections to the hub from the client will automatically pass along this
        cookie.
        """
        response = super(MercureMixin, self).dispatch(request, *args, **kwargs)

        if settings.MERCURE_ENABLED:
            token = mercure.get_jwt_token(
                self.get_mercure_subscribe_targets(),
                self.get_mercure_publish_targets()
            )
            response.set_cookie(
                'mercureAuthorization',
                token,
                httponly=True,
                domain=settings.MERCURE_HUB_COOKIE_DOMAIN,
                path='/',
                secure=settings.MERCURE_HUB_SECURE_COOKIE,
            )

        return response

    def get_context_data(self, **kwargs):
        """
        Adds the Mercure Hub URL to the template context. Views can use this URL to
        connect to the hub from the client. For Intercooler support, this URL should be
        set on a container HTML element using the `ic-sse-src` attribute.
        """
        context = super(MercureMixin, self).get_context_data(**kwargs)
        if settings.MERCURE_ENABLED:
            context['mercure_hub_url'] = mercure.get_hub_url(self.get_mercure_hub_topics())
        return context