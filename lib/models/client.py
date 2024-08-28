from .__init__ import CONN, CURSOR
import re

_name = r"^[A-Za-z]+$"
_name_regex = re.compile(_name)

phone_number = r"(\d{3}-){2}\d{4}"
phone_regex = re.compile(phone_number)

class Client:

    all = {}

    def __init__(self, first_name, last_name, phone_number, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}, {self.phone_number}>"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name) and _name_regex.fullmatch(first_name):
            self._first_name = first_name
        else:
            raise ValueError("First name cannot be empty and contains only letters")
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name) and _name_regex.fullmatch(last_name):
            self._last_name = last_name
        else:
            raise ValueError("Last name cannot be empty and contains only letters")

    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if phone_regex.fullmatch(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError("Enter phone number with the following pattern: 555-555-5555")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            phone_number TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS clients;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO clients (first_name, last_name, phone_number)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.phone_number))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name, phone_number):
        client = cls(first_name, last_name, phone_number)
        client.save()
        return client

    def update(self):
        sql = """
            UPDATE clients
            SET first_name = ?, last_name = ?, phone_number = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.phone_number, self.id))
        CONN.commit()

    def delete(self):
        sql = """
        DELETE FROM clients
        WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        client = cls.all.get(row[0])
        if client:
            client.first_name = row[1]
            client.last_name = row[2]
            client.phone_number = row[3]
        else:
            client = cls(row[1], row[2], row[3])
            client.id = row[0]
            cls.all[client.id] = client
        return client

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM clients
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM clients
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def search(cls, first_name=None, last_name=None, phone_number=None):
        results = []
        print(cls.all)
        for item in cls.all:
            if (first_name is None or item.first_name == first_name) and \
                (last_name is None or item.last_name == last_name) and \
                (phone_number is None or item.phone_number == phone_number):
                results.append(item)
        return results