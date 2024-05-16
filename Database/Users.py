import time

from Database.DatabaseConnection import DatabaseConnection


class UsersDB(DatabaseConnection):

    def get_total_users_count(self):
        db = self.connect_to_db()
        db_cursor = db.cursor()
        db_cursor.execute("SELECT count(*) FROM users;")
        result = db_cursor.fetchone()[0]
        time.sleep(2)
        db.close()
        return result