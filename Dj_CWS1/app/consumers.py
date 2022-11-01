from channels.consumer import SyncConsumer, AsyncConsumer

from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        """
        This handler is called when clinet initially opens a
        connection and is about to finish the WebSocket handshake
        """
        print("WebSocket Connected....", event)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self, event):
        """
        This handler is called when data recived from client
        """
        print("Message Recived.....", event)
        self.send({
            'type':'websocket.send',
            'text': 'Massage from Application to client'
        })

    def websocket_disconnect(self, event):
        """
        This handler is called when either connction to the clinet is lost,
        either from client closing the connection, the server closing the
        connection, or loss of socket.
        """
        print("WebSocket Disconnected.....", event)
        raise StopConsumer()

class MyAyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        """
        This handler is called when clinet initially opens a
        connection and is about to finish the WebSocket handshake
        """
        print("WebSocket Connected....",event)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event):
        """
        This handler is called when data recived from client
        """
        print("Message Recived.....",event)
        await self.send({
            'type':'websocket.send',
            'text': 'Massage from Application to client'
        })

    async def websocket_disconnect(self, event):
        """
        This handler is called when either connction to the clinet is lost,
        either from client closing the connection, the server closing the
        connection, or loss of socket.
        """
        print("WebSocket Disconnected.....",event)
        raise StopConsumer()