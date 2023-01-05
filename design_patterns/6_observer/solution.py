class Client:
    def update_price(self, subject: object, *args, **kwargs):
        pass

class StockExchange:
    def __init__(self):
        self._clients = []
    
    def register_observer(self, client: Client):
        self._clients.append(client)
    
    def unregister_observer(self, client: Client):
        self._clients.remove(client)
    
    def notify_clients(self, *args, **kwargs):
        for client in self._clients:
            client.update_price(self, *args, **kwargs)

class Client1(Client):
    def update_price(self, subject: object, *args, **kwargs):
        print(f'Client1 received event: {args}, {kwargs}')

class Client2(Client):
    def update_price(self, subject: object, *args, **kwargs):
        print(f'Client2 received event: {args}, {kwargs}')

publisher = StockExchange()

client1 = Client1()
client2 = Client2()

publisher.register_observer(client1)
publisher.register_observer(client2)

publisher.notify_clients('Price change', stock='Apple', price=278)