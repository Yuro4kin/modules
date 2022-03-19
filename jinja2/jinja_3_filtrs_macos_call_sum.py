# Jinja2 #3: Фильтры и макросы macro, call 
# рассмотрим фильтры, которые удобно применять для получения более сложных представлений
from jinja2 import Template, escape



# Часто применяемый фильтр – это sum для вычисления суммы определенной коллекции
# Например, у нас имеется список автомобилей, используем sum, чтоб вывести суммарную
# цену для всех автомобилей
cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

# В шаблоне вызываем фильтр sum для коллекции cs, через | указываем фильтр sum
# и говорим, что суммирование нужно производить по атрибуту 'price'
# Используем именованый параметр attribute 'price'
tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
 
print(msg)

# Например, чтоб на выходе получить список, который у нас передается
tpl1 = "Суммарная цена автомобилей {{ cs }}"
tm1 = Template(tpl1)
msg1 = tm1.render(cs = cars)
print(msg1)

# Фильтр может кардинально меенять поведение шаблона
# В общем случае синтаксис фильтра sum, следующий:
#       sum(iterable, attribute=None, start=0)
# start = 0 - это прибавка, которая добавляется к вычисленной сумме, если необходимо

# Например нужно просуммировать список [1,2,3,4,5] 
digs = [1,2,3,4,5]
tpl2 = "Суммарная цена автомобилей {{ cs | sum }}"
tm2 = Template(tpl2)
msg2 = tm2.render(cs = digs)
print(msg2)



# List of Builtin Filters - полный список фильтров
# https://jinja.palletsprojects.com/en/2.11.x/templates/
# abs()float()lower()round()tojson()attr()forceescape()map()safe()trim()batch()format()max()
# select()truncate()capitalize()groupby()min()selectattr()unique()center()indent()
# pprint()slice()upper()default()int()random()sort()urlencode()dictsort()join()reject()
# string()urlize()escape()last()rejectattr()striptags()wordcount()filesizeformat()length()
# replace()sum()wordwrap()first()list()reverse()title()xmlattr()

# Например посчитаем максимальную цену в нашем списке
tpl3 = "Максимальная цена из автомобилей {{ cs | max (attribute='price') }}"
tm3 = Template(tpl3)
msg3 = tm3.render(cs = cars)
print(msg3)

# Например выведем просто марку автомобиля, которому соответсвует максимальная цена
# Поставим в шаблоне круглые скобки, обращаемся к словарю в целом, беря у него model
tpl4 = "Максимальная цена из автомобилей - {{ (cs | max (attribute='price')).model }}"
tm4 = Template(tpl4)
msg4 = tm4.render(cs = cars)
print(msg4)

# min - фильтр
tpl5 = "Мнимальная цена из автомобилей - {{ (cs | min (attribute='price')).model }}"
tm5 = Template(tpl5)
msg5 = tm5.render(cs = cars)
print(msg5)

# random - фильтр
tpl6 = "Выполнен рандомный выбор автомобиля из списка: {{ cs | random  }}"
tm6 = Template(tpl6)
msg6 = tm6.render(cs = cars)
print(msg6)

# replace - фильтр заменим малые о на заглвные О
tpl7 = 'Выполнена замена малые "о" на заглвные "О" : {{ cs | replace("o", "O")  }}'
tm7 = Template(tpl7)
msg7 = tm7.render(cs = cars)
print(msg7)


# Блок filter
# Большую гибкость в применении фильтров дает специальный блок:

# {{% filter <название фильтра> %}
# <фрагмент для применения фильтра>
# {% endfilter %}


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
    ]

# Есть список person, переберем шаблон циклом for, по имени списка применим фильтр upper
# все имена списка person будут написаны заглавными буквами upper или можем сделать lower
tpl8 = '''
    {%- for u in users -%}
    {% filter upper %}{{u.name}}{% endfilter %}
    {% endfor -%}
    '''
 
tm8 = Template(tpl8)
msg8 = tm8.render(users = persons)
print(msg8)


# Макроопределения - macro
# Модуль Jinja поддерживает макроопределения для шаблонов,
# которые весьма полезны, чтобы избежать повторяемых определений в соответствии с принципом
# DRY – Don’t Repeat Yourself (не повторяйся)

# Например, нам необходимо создать несколько полей ввода input в шаблоне HTML-документа
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}
 
<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''

# Формируем и обрабатываем шаблон
tm9 = Template(html)
msg9 = tm9.render()
print(msg9)

# macro input(name, value='', type='text', size=20)
# macro - ключевое слово
# input - имя макроопределения
# name, value='', type='text', size=20 - абор параметров, если они необходимы (если они не нужны - тогда они не пишутся)

# <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}
# атрибут type принимает значение type, по умолчанию это будет text
# атрибут name ринимает значение name,
# атрибут value принимает значение value c флагом экранирования |e
# атрибут size принимает значение size

# Формируем шаблон 
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# input - поле ввода
# name у этого поля ввода - будет принимать значение username, все остальные параметры берутся по умолчанию
# для следующего поля ввода name - уже будет принимать значение email, все остальные параметры берутся по умолчанию
# для следующего поля ввода name - уже будет принимать значение password, все остальные параметры берутся по умолчанию

# <p><input type="text" name="username" value="" size="20">
# <p><input type="text" name="email" value="" size="20">
# <p><input type="text" name="password" value="" size="20">

# Первый параметр username, остальные взяты по умолчанию, далее email и password
# Для каждой строчки сработало макроопределение, на выходе тег <input> с соответствующими параметрами
# Используем этот макрос для создания трех полей input
# По аналогии можно создавать другие макросы и, затем, многократно их использовать в шаблонах



# Вложенные макросы – call - позволяет создавать своего рода вложенные макросы.
# Модуль Jinja имеет специальный синтаксис:

# {% call[(параметры)] <вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}

# Например, мы хотим сформировать вот такой список:
# Alex
#   age:
#   weight: 78.5
# Nick
#   age:
#   weight: 82.3
# Ivan
#   age:
#   weight: 94.0

# На уровне HTML-документа это выглядит так - список, у которого еще есть вложенный список
# <ul>
# <li>Alex 
#    <ul>
#    <li>age: 
#    <li>weight: 78.5
#    </ul>
# <li>Nick 
#    <ul>
#    <li>age: 
#    <li>weight: 82.3
#    </ul>
# <li>Иван 
#    <ul>
#    <li>age: 
#    <li>weight: 94.0
#    </ul>
# </ul>

# Создадим список который будет хранить всю информацию
# Создадим шаблон, который позволяет генерировать такой список на основе коллекции
persons1 = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Nick", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0}
    ]

# Далее пропишем макроопределение в программе, которое будет создавать этот главный список
# Определим макрос, который генерирует начальный список из имен. Его можно представить так:
# Формируем макроопределение, оно называется list_users, мы ему передаем некий список
# внутри макроопределения формируем тег <ul>, внутри теги <li>
# блок for - для перебора элементов этого списка, после каждого тега <li> пишем имя

html1 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} 
{%- endfor %}
</ul>
{%- endmacro %}
 
{{list_users(users)}}
'''
# {{list_users(users)}} - в конце вызываем макроопределение с параметром users
tm9 = Template(html1)
msg9 = tm9.render(users = persons1)
print(msg9)
# параметр users берется из users = persons1, когда мы будем выполнять шаблон
# передадим list persons1 с помощью именованого параметра users
# соответственно будет использован список persons в {{list_users(users)}},
# где далее подставится в list_of_user(list_of_user), где будет ссылка на список persons 
# далее этот список persons перебираем - for u in users
# формируем теи <li>


# caller(u) - вложенный макрос
# А теперь для каждого человека добавим вложенный список с его возрастом и весом.
# И сделаем это через блок call, шаблон будет выглядеть так:
html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}
 
{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm10 = Template(html2)
msg10 = tm10.render(users = persons1)
print(msg10)






