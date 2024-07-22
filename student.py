from db_config import get_db_connection
from mysql.connector import Error

class Student:
    @staticmethod
    def add_student(student_id, name, date_of_birth, grade_level):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO Students (student_id, name, date_of_birth, grade_level)
                    VALUES (%s, %s, %s, %s)
                """, (student_id, name, date_of_birth, grade_level))
                connection.commit()
            except Error as e:
                print(f"Error adding student: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def update_student(student_id, name=None, date_of_birth=None, grade_level=None):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE students SET "
                params = []
                if name:
                    query += "name=%s, "
                    params.append(name)
                if date_of_birth:
                    query += "date_of_birth=%s, "
                    params.append(date_of_birth)
                if grade_level:
                    query += "grade_level=%s, "
                    params.append(grade_level)
                query = query.rstrip(', ') + " WHERE student_id=%s"
                params.append(student_id)
                cursor.execute(query, tuple(params))
                connection.commit()
            except Error as e:
                print(f"Error updating student: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def delete_student(student_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Students WHERE student_id=%s", (student_id,))
                connection.commit()
            except Error as e:
                print(f"Error deleting student: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_student(student_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Students WHERE student_id=%s", (student_id,))
                student = cursor.fetchone()
                return student
            except Error as e:
                print(f"Error retrieving student: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_all_students():
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Students")
                students = cursor.fetchall()
                return students
            except Error as e:
                print(f"Error retrieving students: {e}")
            finally:
                cursor.close()
                connection.close()
