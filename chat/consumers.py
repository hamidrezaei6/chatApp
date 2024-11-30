from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        print(text_data)

    def receiver_function(self, the_data_that_will_come_from_layer):
        print(the_data_that_will_come_from_layer)
