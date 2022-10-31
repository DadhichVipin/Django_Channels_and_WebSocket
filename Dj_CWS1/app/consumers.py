from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        """
        This handler is called when clinet initially opens a
        connection and is about to finish the WebSocket handshake
        """
        print("WebSocket Connected....")

    def websocket_receive(self, event):
        """
        This handler is called when data recived from client
        """
        print("Message Recived.....")

    def websocket_disconnect(self, event):
        """
        This handler is called when either connction to the clinet is lost,
        either from client closing the connection, the server closing the
        connection, or loss of socket.
        """
        print("WebSocket Disconnected.....")

class MyAyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        """
        This handler is called when clinet initially opens a
        connection and is about to finish the WebSocket handshake
        """
        print("WebSocket Connected....")

    async def websocket_receive(self, event):
        """
        This handler is called when data recived from client
        """
        print("Message Recived.....")

    async def websocket_disconnect(self, event):
        """
        This handler is called when either connction to the clinet is lost,
        either from client closing the connection, the server closing the
        connection, or loss of socket.
        """
        print("WebSocket Disconnected.....")