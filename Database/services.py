from Database.DatabaseConnection import DatabaseConnection


class ServicesDB(DatabaseConnection):


    def get_services_total_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM services;")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def options_count_for_service(self, service_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT COUNT(*) FROM options WHERE service_id = {service_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result
