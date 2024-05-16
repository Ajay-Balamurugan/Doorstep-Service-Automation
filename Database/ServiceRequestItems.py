import time

from Database.DatabaseConnection import DatabaseConnection


class ServiceRequestItemsDB(DatabaseConnection):

    def get_service_request_item_status(self, service_request_item_id):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute(f"SELECT status FROM service_request_items WHERE id = {service_request_item_id};")
        result = db_cursor.fetchone()[0]
        db.close()
        return result

    def get_service_request_items_count(self):
        time.sleep(1)
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM service_request_items;")
        result = db_cursor.fetchone()[0]
        time.sleep(1)
        db.close()
        return result