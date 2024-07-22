from db_config import get_db_connection
from mysql.connector import Error

class Grade:
    @staticmethod
    def add_grade(grade_id, student_id, course_id, grade):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO grades (grade_id, student_id, course_id, grade)
                    VALUES (%s, %s, %s, %s)
                """, (grade_id, student_id, course_id, grade))
                connection.commit()
            except Error as e:
                print(f"Error adding grade: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def get_grades_for_student(student_id):
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM grades WHERE student_id=%s", (student_id,))
                grades = cursor.fetchall()
                return grades
            except Error as e:
                print(f"Error retrieving grades: {e}")
            finally:
                cursor.close()
                connection.close()
