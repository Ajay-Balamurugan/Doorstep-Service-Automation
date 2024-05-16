import time

from Database.DatabaseConnection import DatabaseConnection


class EmployeeSlotsDB(DatabaseConnection):

    def get_employee_slots_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM employee_slots;")
        result = db_cursor.fetchone()[0]
        time.sleep(2)
        db.close()
        return result