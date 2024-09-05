from .client import Client

class Trailer:
    def __init__(self, client_renting_trailer, available=True, id=None):
        self.id = id
        self.client_renting_trailer = client_renting_trailer
        self.available = available
    
    @property
    def client_renting_trailer(self):
        return self._client_renting_trailer

    @client_renting_trailer.setter
    def client_renting_trailer(self, client_renting_trailer):
        if isinstance(client_renting_trailer, int) and Client.find_by_id(client_renting_trailer):
            return self._client_renting_trailer = client_renting_trailer
        else:
            raise ValueError("No client found. Ensure that client exists.")

    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, available):
        if self.client_renting_trailer:
            return self._available = False
        else:
            return self._available = True