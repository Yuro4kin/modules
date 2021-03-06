import sqlite3 as sq
# SQLite #6: Оператор JOIN для формирования сводного отчета

# Выполним объединение данных из разных таблиц для формирования сводного отчета.
# Используем оператор JOIN - синтаксис
# JOIN <таблица> ON <условие связывания>

# Например, у нас есть две таблицы sales и users.
# Таблица sales содержит поле user_id (идентификатор пользователя),
# которое является внешним ключом для связывания с таблицей users по полю rowid,
# которое является первичным ключом:

# Например, добавим данные из таблицы sasles  таблице users:
# SELECT name, sex, sales.payments FROM sales
#     список полей сводной табл.
#                   sales.payments - payments берем именно из таблицы sales, а не из таблицы users
#                   FROM sales     - будем подставлять данные из таблицы sales

# JOIN users ON sales.user_id = users.rowid
# JOIN - говорит какую таблицу мы будем связывать с таблицей sales, в данном случае users
# ON sales.user_id = users.rowid  - условие связывания 
# user_id = rowid - должен быть равен, т.е.
# user_id = 1, значит rowid = 1 - это и есть условие связывания
# users.rowid - указываем из какой таблицы берем rowid

# Таблица sales является первичной, данные изначально берутся из таблицы users/.
# То есть, первые два payments оплатил с Alabama с значениями платежей 200 и 300,
# затем, California - платежи 500, потом, снова Alabama и так далее.
# Благодаря объединению данных мы видим не просто id игрока, а его имя,


# Объединять данные из таблиц можно и без оператора JOIN, просто указав их имена
# после ключевого слова FROM, через запятую, например, так:
# SELECT name, sex, sales.payments FROM users, sales
#                                       users - выбираем name, sex - первые два столбца
#                   sales.payments - выбираем payments из таблицы sales
#  В таблице sales - семь записей, подставляем семь разных записей из таблицы sales 
# 
# Здесь была взята первая запись из таблицы users и ей в соответствие были
# поставлены все записи из второй таблицы sales. И так для всех трех.
# В итоге произошло такое своеобразное соединение двух таблиц без какого-либо критерия.
# Но, так тоже можно делать набор данных из двух таблиц, т.к. иногда он тоже используется.


# Теперь давайте вернемся к рассмотрению оператора JOIN в действительности,
# это аналог оператора INNER JOIN, то есть, соединение записей из двух таблиц,
# если соответствия найдены в обеих из них. Чтобы было понятнее о чем речь,
# рассмотрим такой пример. Удалим из таблицы users последнее имя штата с именем «Indiana».
# Теперь, выполняя запрос увидим отсутствие записи с этим штатом:
# SELECT name, sex, sales.payments FROM sales
# JOIN users ON sales.user_id = users.rowid
# Объединение таблиц, если данные есть и в первой и во второй таблице


# Иногда важно иметь все записи из главной таблицы (sales), а дополнительные сведения
# из второй таблицы добавлять, если они там есть. Для такого объединения данных используется
# модификация LEFT JOIN следующим образом:
# SELECT name, sex, sales.payments FROM sales
# LEFT JOIN users ON sales.user_id = users.rowid
# Появилась строчка с удаленными данными NULL NULL 100, был выполнен платеж неизвестным пользователям на 100 

# Реализуем запрос, который будет формировать список ТОП платежей, используя данные обеих таблиц. 
# SELECT user_id, sum(payments) as sum 
# FROM sales
# GROUP BY user_id
# ORDER BY sum DESC

# Поправим запрос, вместо user_id - имя штата
# SELECT name, sex, sum(sales.payments) as payments 
# FROM sales
# JOIN users ON sales.user_id = users.rowid
# GROUP BY user_id
# ORDER BY payments DESC

# В команде SELECT можно указывать несколько операторов JOIN для объединения данных из
# трех, четырех и большего числа таблиц:
# Синтаксис:
# SELECT <поля> FROM <таблица 1>
# JOIN <таблица 2> JOIN <таблица 3> … JOIN <таблица N>
# ON <условие связывания>
# Вот так работает агрегирование таблиц с помощью оператора JOIN в команде с SELECT,
# можем формировать несколько таблиц для формирования сводного отчета.

# Теперь можем вывести данные на сайт или страничку.


