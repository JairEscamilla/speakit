import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class FeedConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_dicard)(
            self.room_group_name,
            self.channel_name
        ) 

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        post = text_data_json['post']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                'type': 'new_post',
                'post': post
            }
        )
    
    def new_post(self, event):
        post = event['post']
        self.send(text_data=json.dumps({
            'post': post
        }))