# SQLite #2: подключение к БД, создание и удаление таблиц
import sqlite3 as sq

# устанавливаем связь с файлом который находится в каталоге
with sq.connect("saper.db") as con:     # контекст менеджера автоматически закрывает базу данных
# con = sq.connect("saper.db")  # !!!!!!!Так открывать БД нельзя
    cur = con.cursor()  # Для взаимодействия с базой данных используем объект Cursor
                        # метод cursor() возвращает экземпляр класса cursor и через переменную cur
                        # осуществляем непосредственно работу


    # Вызовем execute() которому передается sql запрос для работы с базой данных
    # Создали таблицу с именем users
    #              CREATE TABLE users - чтоб не был error CREATE TABLE IF NOT EXISTS users
    #                       IF EXISTS - если существует
    cur.execute("DROP TABLE IF EXISTS users")    # - удаляем таблицу из файла test.db
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")
                    # ограничители NOT NULL , NOT NULL DEFAULT 1,
                    # PRIMARY KEY говорит что поле user_id должно содержать уникальные значения
                    # AUTOINCREMENT - увеличивает поле на 1 всегда

# Обязательно закрыть после работы БД
# вызываем метод close() у объекта connection на который ссылается переменная con
# con.close()           # close() уже не нужен
