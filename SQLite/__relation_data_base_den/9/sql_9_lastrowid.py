import sqlite3 as sq
# SQLite #9: Свойство lastrowid

# Например, представим, что у нас есть еще одна таблица cust,
# которая содержит покупателей машин.
# Причем, если происходит покупка по «trade-in», то прежняя машина
# владельца добавляется в конец таблицы cars, а в таблице cust
# появляется запись с именем покупателя, идентификатором машины
# сданной в «trade-in» и id новой купленной машины
# последнее поле будет содержать id машины которой приобрел покупатель

# Чтобы реализовать SQL-запрос добавления записи в таблицу cust,
# нам нужно знать car_id автомобиля сданного в «trade-in».
# Предположим, что Alex еще не совершил покупку и таблица cars
# не содержит запись с его сданным автомобилем. Добавим авто сначала.
# Выполним следующий запрос вот в такой программе:

# воспользуемся мейжером контекста, связуемся с БД
with sq.connect("cars.db") as con:
    cur = con.cursor()
 
    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_in INTEGER, buy INTEGER);        
    """)# создаем таблицу cust с полями 
 
    cur.execute("INSERT INTO cars VALUES(NULL,'Renault', 1000)")
    # добавляем в таблицу cars машину Renault, которая по «trade-in» сдается и устанавливается цена в 1000

    # когда будет выполнен этот запрос, св-во lastrowid будет содержать id последней записи
    last_row_id = cur.lastrowid
    # воспользуемся этой информацией чтоб сформировать второй запрос
    # запрос в таблицу cust, где у нас будет указан Alex, далее id автомобиля сданного по trade-in
    # возьмем переменную last_row_id , которая содержит это св-во
    # далее автомобиль который он купит buy_car_id со значением 2
    buy_car_id = 2 
    cur.execute("INSERT INTO cust VALUES('Alex', ?, ?)", (last_row_id, buy_car_id))
    
# Открываем БД
# появилась запись Renault c car_id = 31
# далее переходим в таблицу cust и теперь у Alex авто сданное по trade_in содержит index = 31
# Благодаря свойству .lastrowid - ернуло нам индекс последней записи, которая была вставлена в таблицу car
# и мы ее прописали ?, когда обавляли новую запись в таблицу cars  

# Это частая манипуляция с БД, когда что-то добавляем в одну таблицу и нам нужно взять id
# последней записи, чтоб ее прописать в качестве значения поля у другой записи





