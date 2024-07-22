from db_config import get_db_connection
from mysql.connector import Error

class Teacher:
    @staticmethod
    def add_teacher(teacher_id, name, contact_number, subject_taught):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO teachers (teacher_id, name, contact_number, subject_taught)
                    VALUES (%s, %s, %s, %s)
                """, (teacher_id, name, contact_number, subject_taught))
                connection.commit()
            except Error as e:
                print(f"Error adding teacher: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def update_teacher(teacher_id, name=None, contact_number=None, subject_taught=None):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE teachers SET "
                params = []
                if name:
                    query += "name=%s, "
                    params.append(name)
                if contact_number:
                    query += "contact_number=%s, "
                    params.append(contact_number)
                if subject_taught:
                    query += "subject_taught=%s, "
                    params.append(subject_taught)
                query = query.rstrip(', ') + " WHERE teacher_id=%s"
                params.append(teacher_id)
                cursor.execute(query, tuple(params))
                connection.commit()
            except Error as e:
                print(f"Error updating teacher: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def delete_teacher(teacher_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM teachers WHERE teacher_id=%s", (teacher_id,))
                connection.commit()
            except Error as e:
                print(f"Error deleting teacher: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_teacher(teacher_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM teachers WHERE teacher_id=%s", (teacher_id,))
                teacher = cursor.fetchone()
                return teacher
            except Error as e:
                print(f"Error retrieving teacher: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_all_teachers():
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM teachers")
                teachers = cursor.fetchall()
                return teachers
            except Error as e:
                print(f"Error retrieving teachers: {e}")
            finally:
                cursor.close()
                connection.close()
