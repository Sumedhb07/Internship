#  Part C: Interface Simulation with Abstract Methods
# 7.Create an abstract class Vehicle:
# oAbstract methods:
# start_engine()
# stop_engine()
# oImplement concrete subclasses:
# Car
# Motorcycle
# oTest instances for both.
from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Engine is Started"
    def stop_engine(self):
        return "Engine is Stoped"
class Motorcycle(Car):
    def start_engine(self):
        return "Engine is Started"
    def stop_engine(self):
        return "Engine is Stoped"
car = Car()
print(f"Car: {car.start_engine()}")
print(f"Car: {car.stop_engine()}")

motorcycle = Motorcycle()
print(f"MotorCycle: {motorcycle.start_engine()}")
print(f"MotorCycle: {motorcycle.stop_engine()}")


# 8.Create an abstract class Database:
# oAbstract methods:
# connect()
# disconnect()
# execute_query(query)
# oCreate concrete classes:
# MySQLDatabase
# PostgreSQLDatabase
# SQLiteDatabase
from abc import ABC , abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass
    def execute_query(self , query):
        pass
class MySQLDataBase(Database):
    def connect(self):
        return "Connected to My SQL Database"
    def disconnect(self):
        return "Disconnected from MY SQL Database"
    def execute_query(self, query):
        return f"Executed query on MY SQL Database {query}"
class PostgreSQLDatabase(MySQLDataBase):
    def connect(self):
        return "Connected to PostgreSQL Database"
    def disconnect(self):
        return "Disconnected from PostgreSQL Database"
    def execute_query(self, query):
        return f"Executed query on PostgreSQL Database {query}"
class SQLiteDatabase(PostgreSQLDatabase):
    def connect(self):
        return "Connected to SQLite Database"
    def disconnect(self):
        return "Disconnected from SQLite Database"
    def execute_query(self, query):
        return f"Executed query on SQLite Database {query}"
mysql_db = MySQLDataBase()
print(mysql_db.connect())
print(mysql_db.execute_query("SELECT * FROM users"))
print(mysql_db.disconnect())

postgresql_db = PostgreSQLDatabase()
print(postgresql_db.connect())
print(postgresql_db.execute_query("SELECT * FROM users"))
print(postgresql_db.disconnect())

sqllite_db = SQLiteDatabase()
print(sqllite_db.connect())
print(sqllite_db.execute_query("SELECT * FROM users"))
print(sqllite_db.disconnect())






