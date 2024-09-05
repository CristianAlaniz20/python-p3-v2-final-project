from .__init__ import CONN, CURSOR
from .client import Client

class Trailer:
    
    all = {}

    def __init__(self, client_renting_trailer=None, available=None, id=None):
        self.id = id
        self.client_renting_trailer = client_renting_trailer
        self.available = available

    @property
    def client_renting_trailer(self):
        return self._client_renting_trailer

    @client_renting_trailer.setter
    def client_renting_trailer(self, client_renting_trailer):
        if client_renting_trailer:
            if isinstance(client_renting_trailer, int) and Client.find_by_id(client_renting_trailer):
                self._client_renting_trailer = client_renting_trailer
            else:
                raise ValueError("No client found. Ensure that client exists.")
        else:
            self._client_renting_trailer = client_renting_trailer

    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, available):
        if self.client_renting_trailer:
            self._available = False
        else:
            self._available = True

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
    def create(cls, client_renting_trailer=None, available=None):
        trailer = cls(client_renting_trailer, available)
        trailer.save()
        return trailer

    def update(self):
        sql = """
            UPDATE trailers
            SET client_renting_trailer = ?, available = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.client_renting_trailer, self.available, self.id))
        CONN.commit()

    def delete(self):
        sql = """
        DELETE FROM trailers
        WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        trailer = cls.all.get(row[0])
        if trailer:
            trailer.client_renting_trailer = row[1]
            trailer.available = row[2]
        else:
            trailer = cls(row[1], row[2])
            trailer.id = row[0]
            cls.all[trailer.id] = trailer
        return trailer

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM trailers
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM trailers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None