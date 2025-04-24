from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from sockpuppet.routing import channel_routing
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            channel_routing
        )
    ),
})