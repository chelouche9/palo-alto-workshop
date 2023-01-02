class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class DB(Singleton):
    def __init__(self, connection: str):
        self.connection = connection

db = DB('first connection')
db_two = DB('second connection')
print(db.connection)
print(db_two.connection)