from .__init__ import CONN, CURSOR
from .client import Client

class Trailer:
    
    all = {}
    
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

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trailers (
            id INTEGER PRIMARY KEY,
            client_renting_trailer INTEGER,
            available BOOLEAN)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trailers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trailers (client_renting_trailer, available)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.client_renting_trailer, self.available))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, client_renting_trailer, available):
        trailer = cls(client_renting_trailer, available)
        trailer.save()
        return trailer