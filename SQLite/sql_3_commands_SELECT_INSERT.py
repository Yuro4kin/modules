# SQLite #3: команды-запросы SELECT и INSERT при работе с таблицами БД

# INSERT – добавление записи в таблицу;
# SELECT – выборка данных из таблиц (в том числе и при создании сводной выборки из нескольких таблиц).

# Синтаксис                 поля в которые записываем данные        <---  соответств. данные которые будут записаны в поля        
# INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, …)
# или так:                  данные будут записаны во все поля по порядку
# INSERT INTO <table_name> VALUES (<value1>, <value2>, …)

# INSERT INTO users VALUES (1,'Alex', 1, 19, 1000) - обращать внимание на колличество полей
# INSERT INTO users(name, old, score) VALUES ('Fedor', 34, 200) - добавление данных по определенным полям 

# Синтаксис: поля кот. хотим выбрать
# SELECT col1, col2, … FROM <table_name>
# SELECT name, old, score FROM users - выбрать поля по названию данных
# SELECT name, old, score FROM users - выбрать все поля

# Синтаксис
# Если нам нужно добавить фильтр для выбираемых записей, то это делается с помощью
# ключевого слова WHERE, которое записывается после имени таблицы:
# SELECT col1, col2, … FROM <table_name> WHERE <условие>
# SELECT * FROM users WHERE score < 1000 - выбираем поле score, число очков должно быть меньше < 1000

# В качестве сравнения можно использовать следующие операторы:
# = или ==, >, <, >=, <=, !=, BETWEEN
# SELECT * FROM users WHERE score BETWEEN 500 and 1000 - удут выбраны все данные пользователя у которых кол-во очков в интервале от 500 до 1000
# SELECT * FROM users WHERE score == 200 - кол-во очков = 200

# Составные условия
# AND -> NOT -> OR
# Приоритет AND, затем OR. Если меняем приоритет условий тогда  AND (...OR...) - ставим скобки
# AND – условное И: exp1 AND exp2. Истинно, если одновременно истинны exp1 и exp2.
# OR – условное ИЛИ: exp1 OR exp2. Истинно, если истинно exp1 или exp2 или оба выражения.
# NOT – условное НЕ: NOT exp. Преобразует ложное условие в истинное и, наоборот, истинное – в ложное.
# IN – вхождение во множество значений: col IN (val1, val2, …)
# NOT IN – не вхождение во множество значений: col NOT IN (val1, val2, …)

# SELECT * FROM users WHERE old > 20 AND score < 1000   - возраст игроков больше 20 лет и число очков меньше 1000
# SELECT * FROM users WHERE old IN(19, 39) AND score < 1000 - возраст игроков 19,39 и число очков меньше 1000
# SELECT * FROM users WHERE old IN(19, 39) AND score <= 1000 - возраст игроков 19,39 и число очков меньше или равно 1000
# SELECT * FROM users WHERE old IN(19, 39) AND score <= 1000 OR sex = 1  - возраст игроков 19,39 и число очков меньше или равно 1000 и пол равен 1
# SELECT * FROM users WHERE old IN(19, 39) AND (score > 300 OR sex = 1)  - меняем приоритет
# SELECT * FROM users WHERE (old IN(19, 39) OR sex = 1) AND score > 300
# SELECT * FROM users WHERE old IN(19, 39) AND NOT score > 300

# Сортировка ORDER BY - сортировка по указоному столбцу
# Все записи отсортированы по ВОЗРАСТАНИЮ  возрасту - ORDER BY old ASK
# Все записи отсортированы по УБЫВАНИЮ  возрасту - ORDER BY old DESK
# SELECT * FROM users
# WHERE old IN(19, 39) AND score <= 1000 OR sex = 1
# ORDER BY old ASC
# SELECT * FROM users WHERE score < 1000 ORDER BY old


# LIMIT 2 - сколько записей мы будем отбирать из нашей выборки
# LIMIT <max> [OFFSET offset] - OFFSET означает пропустить записи и перейти к следующим
# LIMIT <offset, max>         - эквивалентная запись < смещение, кол-во записей >

# число очков должно быть не менее 100, затем, данные сортируются по убыванию очков и отбираются первые пять записей
# SELECT * FROM users
# WHERE score > 100 ORDER BY score DESC LIMIT 5

# параметр OFFSET позволяет пропускать несколько первых записей, в нашем примере 2 записи
# SELECT * FROM users
# WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2
# эквивалентная запись:
# SELECT * FROM users
# WHERE score > 100 ORDER BY score DESC LIMIT 2, 5




import sqlite3 as sq

# устанавливаем связь с файлом который находится в каталоге
with sq.connect("saper_3.db") as con:     # контекст менеджера автоматически закрывает базу данных
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
