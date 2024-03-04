from faker import Faker
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

faker = Faker()


# Функція для створення з'єднання
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='password',
            host='localhost'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except Error as e:
        print(f"Помилка при підключенні до бази даних: {e}")
        return None


# Функція для вставки даних в таблицю users
def create_users(conn, fullname, email):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()
    except Error as e:
        print(f"Помилка при вставці даних: {e}")
    finally:
        cursor.close()


# Функція для вставки даних в таблицю tasks
def create_tasks(conn, title, description, status_id, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                       (title, description, status_id, user_id))
        conn.commit()
    except Error as e:
        print(f"Помилка при вставці даних: {e}")
    finally:
        cursor.close()




if __name__ == "__main__":
    # Створення з'єднання
    conn = create_connection()

    if conn is not None:
        try:
            # Генерація даних для users
            for _ in range(10):
                fullname = faker.name()
                email = faker.email()
                create_users(conn, fullname, email)

            # Генерація даних для tasks
            for user_id in range(1, 11):  
                for _ in range(5):  
                    title = faker.sentence(nb_words=6)
                    description = faker.text(max_nb_chars=200)
                    status_id = faker.random_int(min=1, max=3) 
                    create_tasks(conn, title, description, status_id, user_id)
        finally:
            # Закриття з'єднання
            conn.close()