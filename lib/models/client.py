from .__init__ import CONN, CURSOR
import re

phone_number = r"(\d{3}-){2}\d{4}"
phone_regex = re.compile(phone_number)

class Client:

    all = {}

    def __init__(self, first_name, last_name, phone_number, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and len(first_name):
            self._first_name = first_name
        else:
            raise ValueError("First name cannot be empty")
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and len(last_name):
            self._last_name = last_name
        else:
            raise ValueError("Last name cannot be empty")

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

    