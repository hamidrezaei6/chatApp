from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data = json.loads(text_data)
        print(text_data.get('type'))
        print(text_data.get('message'))

    def receiver_function(self, the_data_that_will_come_from_layer):
        print(the_data_that_will_come_from_layer)
