# SQLite #5: Агрегирование и группировка GROUP BY

# Рассмотрим агрегирующие функции, используемые в языке SQL.
# Выполним группировку записей по определенному полю.
# Все эти операции доступны в команде SELECT

# Рассмотрим пример подсчета числа записей таблицы users,
# в которых были покупеи с user_id = 1, определим запрос:
# ф-ция  count - агрегирует, определяет число записей которые попали в нашу выборку
# SELECT count(user_id) FROM users WHERE user_id = 1
# SELECT count(payments) FROM users WHERE payments = 300
# SELECT count(delivery_time) FROM users WHERE delivery_time = 20

# alias - синоним для запроса
# SELECT count(delivery_time )as time FROM users WHERE delivery_time = 20
# теперь поле называется time - им уже удобней пользоваться

# SELECT можно использовать следующие наиболее распространенные агрегирующие функции:
# count() – подсчет числа записей;
# sum() – подсчет суммы указанного поля по всем записям выборки;
# avr() – вычисление среднего арифметического указанного поля;
# min() – нахождение минимального значения для указанного поля;
# max() – нахождение максимального значения для указанного поля.


# Подсчитаем в таблице users число уникальных покупателей.
# запишем вот такой SQL-запрос:
# SELECT count(DISTINCT user_id) as count FROM users
# SELECT DISTINCT user_id as count FROM users
# DISTINCT - указывает СУБД выбирать записи с уникальными user_id

# Затем, с помощью агрегирующей функции count мы вычисляем число
# таких записей и получаем количество уникальных игроков.
# Чтобы все это было понятнее, можно выполнить запрос без агрегирующей функции:
# SELECT DISTINCT user_id FROM users

# Предположим, что нам нужно подсчитать суммарное число платежей,
# которое набрал игрок с user_id = 1 за все время
# SELECT sum (payments) as sum FROM users WHERE user_id = 1


# Также можно брать максимальный или минимальный платеж
# SELECT max(payments) FROM users WHERE user_id = 1
# SELECT min(payments) FROM users WHERE user_id = 1

# Группировка GROUP BY
# Язык SQL позволяет вызывать агрегирующие функции не для всех записей в выборке,
# а локально для указанных групп. Например, мы хотим на основе нашей таблицы
# users создать список ТОП лучших покупателей. Для этого нужно вызвать функции sum
# для каждого уникального user_id.
# Используем оператор
# GROUP BY <имя поля>
# который группирует записи по указанному столбцу.
# В этом случае агрегирующие функции будут работать в пределах каждой группы:

# SELECT user_id, sum(payments) as sum 
# FROM users 
# GROUP BY user_id

# Отсортируем таблицу по убыванию платежей, в конец созданного запроса добавим оператор
# ORDER BY sum DESC

# Добавим еще фильтр для выбора записей с значением платежей более 300:
# SELECT user_id, sum(payments) as sum 
# FROM users
# WHERE payments > 300 
# GROUP BY user_id
# ORDER BY sum DESC

# Нужно задать ограничение по числу отбираемых записей, то в последнюю очередь записывается оператор LIMIT:
# SELECT user_id, sum(payments) as sum 
# FROM users
# WHERE payments > 300 
# GROUP BY user_id
# ORDER BY sum DESC
# LIMIT 1







