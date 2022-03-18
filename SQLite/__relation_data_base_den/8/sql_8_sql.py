import sqlite3 as sq
# SQLite #8: Вложенные SQL запросы к СУБД

# Например у нас есть две таблицы
# Первая customers содержит информацию о покупателях,
# вторая payments – их цены по разным товарам
# Каждый из покупателей (кроме четвертого) покупал товар L'Oreal Paris Telescopic Extra-Black
# От нас требуется выбрать всех окупателей, у которых платежи по товару L'Oreal Paris Telescopic Extra-Black
# выше, чем у Anny (клиент с id = 2)
# По идее нам тут нужно реализовать два запроса:
#   - первый получает значение цены для Anny по товару L'Oreal Paris Telescopic Extra-Black
#   - для всех покупателей, у которых цена выше чем у Anny на товар L'Oreal Paris Telescopic Extra-Black

# SELECT cost FROM payments
# WHERE id = 2 AND products LIKE 'L`Oreal Paris Telescopic Extra-Black'
# Выбираем cost по товару L'Oreal Paris Telescopic Extra-Black для Anny,
# т.е. id = 2 - это покупатель Anny  

# Например, выберем всех покупателей, у которых платежи выше чем у Anny
# Формируем сводную таблицу из имени покупателя, названия товара, его стоимости
# далле выбираем все эти поля из таблицы payments и из таблицы customers
# указываем условия связывания, чтоб rowid у таблицы customers == совпадал с id таблицы payments 
# далее условие WHERE, тоб платежи были больше 295, посмотрели по отчету что
# платеж у Anny былбольше равен 295, поэтому явно прописываем 295
# и еще ставим условие, что товар мы вибираем 'L`Oreal Paris Telescopic Extra-Black'

# Выделяем только запрос в три строки и нажиаем Crl+Enter
# SELECT name, products, cost FROM payments
# JOIN customers ON customers.rowid = payments.id
# WHERE cost > 295 AND products LIKE 'L`Oreal Paris Telescopic Extra-Black'
# Получаем двух покупателей, которые оплатили 324 по товару L`Oreal Paris Telescopic Extra-Black

# В языке SQL - эти два запроса можно объединить в один - используем вложеные запросы
# В скобках () записываем первый запрос вместо 295
# Первым выполняется вложенный запрос в скобках - определяется цена для Anny,
# Вторым выполняется внешний запрос - в котором определяются покупатели с платежами выше чем у Anny

# SELECT name, products, cost FROM payments
# JOIN customers ON customers.rowid = payments.id
# WHERE cost > ( SELECT cost FROM payments
# WHERE id = 2 AND products LIKE 'L`Oreal Paris Telescopic Extra-Black')
# AND products LIKE 'L`Oreal Paris Telescopic Extra-Black'


# Если мы в вложенном запросе запишем (SELECT cost FROM payments WHERE id = 2)
# результат будет такой же, т.к. другие результаты полностью игнорируются
# SELECT name, products, cost FROM payments
# JOIN customers ON customers.rowid = payments.id
# WHERE cost > ( SELECT cost FROM payments WHERE id = 2 )
# AND products LIKE 'L`Oreal Paris Telescopic Extra-Black'

# Обратим внимание, что подзапросы не могут обрабатывать свои результаты,
# поэтому в них нельзя указывать, например, оператор GROUP BY.
# Но агрегирующие функции можно использовать
# Агрегирующие функции для вложенных запросов - вычислим среднее арифметическое
# Получим тоже самое
# У Anny средний платеж 
# SELECT name, products, cost FROM payments
# JOIN customers ON customers.rowid = payments.id
# WHERE cost > ( SELECT avg(cost) FROM payments WHERE id = 2 )
# AND products LIKE 'L`Oreal Paris Telescopic Extra-Black'
# меняем знак на < - получаем платежи меньшие чем средний платеж у Anny


# Вложенные запросы можно использовать и в команде INSERT
# Предположим, что у нас имеется вот такая таблица female - она идентична таблице
# customers - со списком покупателей.
# Например нужно добавить в таблицу female всех покупателей женского пола
# для начала отберем всех покупателей женского пола из таблицы customers
# Запрос SQL:
# SELECT * FROM customers WHERE sex = 2
# Чтоб вставить полученные строчки в таблицу female
# INSERT INTO female
# SELECT * FROM customers WHERE sex = 2
# так можно объединять два запроса SELECT, INSERT чтоб добавить в таблицу данные
# недостаток: ERROR - если вызвать еще один раз
# таблица female - id должен быть PRIMARY KEY
# Запрос SQL:
# INSERT INTO female
# SELECT NULL, name, sex, old FROM customers WHERE sex = 2

# Можем создавать и вложенные запросы для UPDATE
# Например, нужно обнулить все значения цены cost таблицы payments, которые меньше
# или равны минимального платежа покупателя с id = 1
# т.е. все платежи которые меньше или равны 296 должны быть обнулены
# Запрос SQL:
# UPDATE payments SET cost = 0
# WHERE cost <= (SELECT min(cost) FROM payments WHERE id = 1)
# первым выполняется запрос в круглых скобках - вернет минимальный платеж
# для первого клиента c id = 1, потом будет выполняться сравнение и изменение соответствующих записей

# Вложения в команде DELETE
# аналогичные действия можно выполнять и в команде DELETE
# Например, требуется удалить из таблицы customers всех name, возраст которых меньше,
# чем у Anny (customer с id = 2)
# Запрос SQL:
# DELETE FROM customers
# WHERE old < (SELECT old FROM customers WHERE id = 2)
# вложенные запросы в языке SQL - прибегать к ним следует в последнюю очередь,
# если никакими другими командами не удается решить поставленную задачу.
# Так как они создают свое отдельное обращение к БД и на это тратятся дополнительные
# вычислительные ресурсы.

# Мы лишь рассмотрели примеры, принцип создания вложенных запросов.
# На практике они могут разрастаться и становиться довольно объемными,
# включать в себя различные дополнительные операции для выполнения
# нетривиальных действий с таблицами БД.


















