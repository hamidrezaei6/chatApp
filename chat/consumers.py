from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from . import models
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print(self.channel_name)

        self.person_id = self.scope.get('url_route').get('kwargs').get('id')

    def receive(self, text_data):
        text_data = json.loads(text_data)


        new_message = models.Message()
        new_message.from_who = self.scope.get('user')
        new_message.to_who = User.objects.get(id=self.person_id)
        new_message.message = text_data.get('message')
        new_message.date = '2024-12-15'
        new_message.time = '20:12:10'
        new_message.has_been_seen = False
        new_message.save()

        data = {
            'type':'receiver_function',
            'type_of_data' : 'new_message',
            'data': text_data.get('message')
        }

        async_to_sync(self.channel_layer.send)('name_channel',data)
    def receiver_function(self, the_data_that_will_come_from_layer):
        print(the_data_that_will_come_from_layer)
