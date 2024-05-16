import mysql.connector

class DatabaseConnection:
    def __init__(self):
        pass

    def connect_to_db(self):
        doorstep_service_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="AAAB8132",
            database='door_step_service_development'
        )

        return doorstep_service_db