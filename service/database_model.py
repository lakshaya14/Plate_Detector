import pyodbc
import datetime
import config

class DatabaseHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
            self.conn = pyodbc.connect(config.CONNECTION_STRING)
            self.cursor = self.conn.cursor() 
            print("Database connection successful.")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def store_plate(self, number_plate, accuracy, status, direction):
        if not self.conn or not self.cursor:
            print("Cannot store plate, no database connection.")
            return
        try:
            timestamp = datetime.datetime.now()
            sql = "INSERT INTO VehiclePlate (NumberPlate, Time, Accuracy, Status, Direction) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (number_plate, timestamp, accuracy, status, direction))
            self.conn.commit()
            print(f"Stored to DB: {number_plate}")
        except pyodbc.Error as e:
            print(f"Error storing plate to DB: {e}")

    def fetch_all_records(self):
        if not self.conn or not self.cursor:
            print("Cannot fetch records, no database connection.")
            return []
        try:
            self.cursor.execute("SELECT * FROM VehiclePlate") 
            records = self.cursor.fetchall()
            return records
        except pyodbc.Error as e:
            print(f"Error fetching records: {e}")
            return []

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    