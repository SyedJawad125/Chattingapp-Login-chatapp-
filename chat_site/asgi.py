"""
ASGI config for chat_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack # type: ignore
from channels.routing import ProtocolTypeRouter,URLRouter # type: ignore
from channels.security.websocket import AllowedHostsOriginValidator # type: ignore
from chatapp.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_site.settings')

application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket" : AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
    }
)



# import os

# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter,URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from chatapp.routing import websocket_urlpatterns

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatweb.settings')

# asgiapplication = get_asgi_application()

# application = ProtocolTypeRouter(
#     {
#         "http": asgiapplication,
#         "websocket" : AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
#         )
#     }
# )