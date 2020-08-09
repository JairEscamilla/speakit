import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from posts.models import Post

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
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        ) 

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        post = text_data_json['post']
        username = text_data_json['username']

        user = User.objects.filter(username=username).first()

        new_post = Post(post=post, user=user)
        new_post.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                'type': 'new_post',
                'post': post,
                'username': username,
                'created_at':  str(new_post.created_at),
                'id': new_post.id
            }
        )
    
    def new_post(self, event):
        post = event['post']
        self.send(text_data=json.dumps({
            'post': post,
            'username': event['username'],
            'created_at': event['created_at'],
            'id': event['id']
        }))