"""
ASGI config for whatsapp_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_clone.settings')
from django.urls import path
from channels.routing import protocolTypeRouter,URLRouter
from channels.auth import AuthMiddleware
from chat.consumer import personalChatConsumer
application = get_asgi_application()

application = protocolTypeRouter({
    'websocket':AuthMiddleware(
        URLRouter([
            path('ws/<int:id>/',personalChatConsumer),
        ])
    )
})