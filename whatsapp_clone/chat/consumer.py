import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class personalChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['utl_route']['kwarg']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()
    
    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username
            }
        )

    async def chat_message(self,event):
        message  = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username 
        }))

        
        
