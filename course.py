from db_config import get_db_connection
from mysql.connector import Error

class Course:
    @staticmethod
    def add_course(course_id, name, teacher_id, maximum_students):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO courses (course_id, name, teacher_id, maximum_students)
                    VALUES (%s, %s, %s, %s)
                """, (course_id, name, teacher_id, maximum_students))
                connection.commit()
            except Error as e:
                print(f"Error adding course: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def update_course(course_id, name=None, teacher_id=None, maximum_students=None):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE courses SET "
                params = []
                if name:
                    query += "name=%s, "
                    params.append(name)
                if teacher_id:
                    query += "teacher_id=%s, "
                    params.append(teacher_id)
                if maximum_students:
                    query += "maximum_students=%s, "
                    params.append(maximum_students)
                query = query.rstrip(', ') + " WHERE course_id=%s"
                params.append(course_id)
                cursor.execute(query, tuple(params))
                connection.commit()
            except Error as e:
                print(f"Error updating course: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def delete_course(course_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM courses WHERE course_id=%s", (course_id,))
                connection.commit()
            except Error as e:
                print(f"Error deleting course: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_course(course_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM courses WHERE course_id=%s", (course_id,))
                course = cursor.fetchone()
                return course
            except Error as e:
                print(f"Error retrieving course: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_all_courses():
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM courses")
                courses = cursor.fetchall()
                return courses
            except Error as e:
                print(f"Error retrieving courses: {e}")
            finally:
                cursor.close()
                connection.close()
