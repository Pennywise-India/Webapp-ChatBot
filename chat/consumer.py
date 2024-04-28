import json,requests
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # print("hello")
        self.accept()
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json['text'])
        
        response = requests.post("http://127.0.0.1:5000/message", 
        data={"message": text_data_json['text']},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        print(response.text)
       
        self.send(text_data=json.dumps({"message": response.text}))
        
        # async_to_sync(self.channel_layer.send)(
        #     self.channel_name,
        #     {
        #         "type": "chat_message",
        #         "text": {"msg":response.text, "source": "user"},
        #     },
        # )

    def chat_message(self, event):
        text = event["text"]
        print(event["source"])
        self.send(text_data=json.dumps({"text": text}))