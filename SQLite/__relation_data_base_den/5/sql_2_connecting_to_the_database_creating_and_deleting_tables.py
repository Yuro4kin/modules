import sqlite3 as sq
# SQLite #2: подключение к БД, создание и удаление таблиц

# устанавливаем связь с файлом который находится в каталоге
with sq.connect("sales.db") as con:     # контекст менеджера автоматически закрывает базу данных
# con = sq.connect("saper.db")  # !!!!!!!Так открывать БД нельзя
    cur = con.cursor()  # Для взаимодействия с базой данных используем объект Cursor
                        # метод cursor() возвращает экземпляр класса cursor и через переменную cur
                        # осуществляем непосредственно работу
    print(type(con))
    print(type(cur))
    # Вызовем execute() которому передается sql запрос для работы с базой данных
    # Создали таблицу с именем users
    #              CREATE TABLE users - чтоб не был error CREATE TABLE IF NOT EXISTS users
    #                       IF EXISTS - если существует



#    - удаляем таблицу из файла sales.db, и указываем таблицу которая удаляется
#    cur.execute("DROP TABLE IF EXISTS users")

#                   Комагды и типы заглавными буквами

    cur.execute("""CREATE TABLE IF NOT EXISTS users (

           user_id INTEGER PRIMARY KEY AUTOINCREMENT,
           payments INTEGER,
           delivery_time INTEGER
           )""")
                    # ограничители NOT NULL , NOT NULL DEFAULT 1, - поле TEXT всегда заполнено данными 
                    # PRIMARY KEY говорит что поле user_id должно содержать уникальные значения
                    # AUTOINCREMENT - увеличивает поле на 1 всегда
print(type(cur))

# Обязательно закрыть после работы БД
# вызываем метод close() у объекта connection на который ссылается переменная con
con.close()    

# close() уже не нужен

##  Чтобы знать как прописывать типы полей, приведем их полный список:
##    NULL – значение NULL;
##    INTEGER – целочисленный тип (занимает от 1 до 8 байт);
##    REAL – вещественный тип (8 байт в формате IEEE);
##    TEXT – строковый тип (в кодировке данных базы, обычно UTF-8);
##    BLOB (двоичные данные, хранятся «как есть», например, для небольших изображений). 

