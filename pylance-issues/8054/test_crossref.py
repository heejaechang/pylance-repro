class Client:
    def connect(self) -> None: ...
    def disconnect(self) -> None:
        """Disconnect from the server after :meth:`connect`"""  # This works

def connect_client(client: Client) -> None:
    """Call :meth:`Client.connect`."""  # This doesn't work
