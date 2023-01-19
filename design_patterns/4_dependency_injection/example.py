# Database interface
class IDatabase:
    def connect(self):
        pass
    
    def query(self, query: str):
        pass
    
    def close(self):
        pass

# MySQL database implementation
class MySQLDatabase(IDatabase):
    def connect(self):
        print('Connecting to MySQL database...')
    
    def query(self, query: str):
        print(f'Executing query: {query}')
    
    def close(self):
        print('Closing MySQL connection...')

# DataAccess class that receives a database object through dependency injection
class DataAccess:
    def __init__(self, db: IDatabase):
        self.db = db
    
    def execute_query(self, query: str):
        self.db.connect()
        self.db.query(query)
        self.db.close()

# Create a MySQLDatabase object
mysql = MySQLDatabase()

# Create a DataAccess object and inject the MySQLDatabase object as a dependency
data_access = DataAccess(mysql)

# Execute a query using the DataAccess object
data_access.execute_query('SELECT * FROM users')