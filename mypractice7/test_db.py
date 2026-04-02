import psycopg2
from config import host, database, user, password

try:
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    print("УРА! ПОДКЛЮЧЕНИЕ УСПЕШНО!")
    conn.close()
except Exception as e:
    print(f"ОШИБКА: {e}")