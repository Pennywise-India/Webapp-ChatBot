import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # print("hello")
        self.accept()
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json['text'])
        self.send(text_data=json.dumps({"message": text_data_json['text']}))
        
        # async_to_sync(self.channel_layer.send)(
        #     self.channel_name,
        #     {
        #         "type": "chat_message",
        #         "text": {"msg": text_data_json["text"], "source": "user"},
        #     },
        # )

    # def chat_message(self, event):
    #     text = event["text"]
    #     print(event["source"])
    #     self.send(text_data=json.dumps({"text": text}))