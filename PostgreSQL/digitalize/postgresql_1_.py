# postgresql_1_
# Разработка системы, разработка интернет- магазина
# сущность - entity - что-то, о чем нужно хранить информацию в БД
# отдельная сущность в интернет магазине: клиент, заказ, продукт, фотография продукта,
# берем большую задачу, разбиваем ее на блоки и выявляем сущности
# 1. выявить сущности
# 2. выявить набор данных по каждой сущности
# 3. выявить взаимосвязи между сущностями

# В каждой сущности есть свои поля
# Какие поля есть в клиенте покупателе: это его имя, это его телефон, это его e-mail
# Какие есть поля в товаре: это его название, это его описание, это его цена
# Какие есть поля в фотографии товара: это url - ссылка на изображение

# По каждой сущности у нас есть набор полей.
# Cущность в БД - это таблица,  которой отдельные колонки составляют поля этой сущности.

# Например у нас есть customer - клиент в интернет-магазине,
# где каждая строка в таблице - это новый клиент, а каждая колонка - это отдельное поле по клиенту
# Колонки представляют поля этой сущности.

# Relation DB - это связь, т.е. разные сущности могут быть связаны друг с другом
# фотография товара должна ссылаться на этот товар, это и есть связь,
# разные таблицы в БД могут быть связаны друг с другом - в этом и есть основа Relation DB

# Старт проекта - это схема БД - ERD схема
# Схема БД интернет-магазина, идентификаторы - это поля по каждой таблице

# первая сущность - customer - клиент: с полями id, name, phone, email
# вторая сущность - product: с полями id, name, description, price
# третья сущность - product-photo: с полями id, url, product_id
# четвертая сущность - cart - корзина: с полями id, customer_id
# пятая сущность - cart-product: с полями cart_id(ссылка на корзину), product_id(ссылка на товар)

# поле product_id сущности product-photo ссылается на поле id сущности product
# поле customer_id cущности cart ссылается на поле id сущности customer

# Теперь у нас есть customer - это клиент, есть product - то товар в нашем магазине
# есть фотографии товаров product-photo, фотография ссылается на продукт, т.е. фотография относится к какому-то продукту
# есть корзина - cart, заказ,  каждая корзина ссылается на какого-то customer, т.е. на какого-то клиента
# есть связующая таблица (cart-product) которая связывает товары и корзину, потому что
# в одной корзине могут быть несколько товаров и разные товары могут быть в разных корзинах
# т.е. отношение многие ко многим, один товар может принадлежать разным корзинам
# и в одной корзине могут быть много разных товаров, (отношение многих ко многим)
# здесь отношение - один ко многим, т.е. в одном продукте может быть несколько фотографий, но
# каждая фотография относится к одному продукту


# Теперь можно переносить структуру в БД, создавать поля, указываем связи между ними
# Создаем БД shop 
# 10:30





