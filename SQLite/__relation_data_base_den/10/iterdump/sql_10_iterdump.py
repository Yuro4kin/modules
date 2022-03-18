import sqlite3 as sq
# SQLite #10: Создание бэкапа БД

# Рассмотрим Класс Cursor содержит один весьма полезный метод iterdump()
# возвращающий итератор для SQL-запросов, на основе которых можно воссоздать текущую БД.
# Если просто вывести в консоль возвращаемых строк
# Например, как это можно использовать

# если мы подключимся к нашей БД cars и используем метод iterdump()
with sq.connect("cars.db") as con:
    cur = con.cursor()
    # с помощью цикла for мы можем получить список запросов для формирования таблиц БД cars
    for sql in con.iterdump():
        print(sql)


# на выходе получим, сначала формируем таблицу cars, наполняем значениями
# далее формируется таблица users с соответствующими полями
# выполняя эти команды мы воссоздадим наши таблицы

##    BEGIN TRANSACTION;
##    CREATE TABLE cars (
##                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
##                model TEXT,
##                price INTEGER);
##    INSERT INTO "cars" VALUES(1,'Audi',0);
##    INSERT INTO "cars" VALUES(2,'Mercedes',57127);
##    INSERT INTO "cars" VALUES(3,'Skoda',9000);
##    INSERT INTO "cars" VALUES(4,'Volvo',29000);
##    INSERT INTO "cars" VALUES(5,'Bentley',350000);
##    DELETE FROM "sqlite_sequence";
##    INSERT INTO "sqlite_sequence" VALUES('cars',5);
##    CREATE TABLE users (
##                name TEXT,
##                ava BLOB,
##                score INTEGER);
##    INSERT INTO "users" VALUES('Николай', …,1000);
##    COMMIT;

# чтоб наша программа была функциональная все строчки сохраним в отдельном файле
# открываем файл на запись, далее вызываем цикл for
# в файле будут находиться конструкции языка sql с помощью которых мы можем воссоздать таблицы БД
#    with open("sql_damp.sql", "w") as f:
#        for sql in con.iterdump():
#            f.write(sql)

# воспользуемся файлом sql_damp.sql, чтоб восстановить БД, допустим БД потерялась
# открываем файл на чтение, читаем все SQL запросы
# выполняем метод executescript(sql), который выполнит все sql запросы
    with open("sql_damp.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)

# Так можно создавать damp БД, и на основе его восстанавливать БД






            
    

