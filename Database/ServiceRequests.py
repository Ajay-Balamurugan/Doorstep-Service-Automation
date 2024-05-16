from Database.DatabaseConnection import DatabaseConnection


class ServiceRequestsDB(DatabaseConnection):

    def get_service_requests_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM service_requests;")
        result = db_cursor.fetchone()[0]
        db.close()
        return result