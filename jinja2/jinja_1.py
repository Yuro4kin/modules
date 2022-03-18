# Jinja2 #1: О шаблонизаторе, использование {{ }} в шаблонах
# служит для обработки шаблонов в Python, шаблонизатором можно пользоваться в своих приложениях
# Модули для использования - Flask, Django
# Documetation: https://jinja.palletsprojects.com/en/2.11.x/
# {{}} - функционал модуля Jinja который позволяет на выходе получать простые строковые значения
from jinja2 import Template



name = "Yuriy"

# С помощью класса Template, которого импортировали с модуля jinja2 сформируем шаблон
# Создаем экземпляр класса Template на основе текстового шаблона ("Hello {{ name }}")
# Шаблон вместо определения {{ name }} подставляет соответствующее значение
# Подстановка делается с помощью метода .render() класса Template и далее создается именованный параметр
# name со значением Yuriy
# на выходе метод .render() возвращает готовый шаблон, этот готовый шаблон мы выводим в консоль
tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)
print(type(tm))
print(type(msg))

# Какие конструкции можно писать внутри шаблонов
# метод render класса Tempalte понимает следующие определения:
# · {% %} – спецификатор шаблона;
# · {{ }} – выражение для вставки конструкций Python в шаблон;
# · {# #} – блок комментариев;
# · # ##  – строковый комментарий.

# Именованые параметры внутри метода .render воспринимаются как словарь n=name1
# мы формируем словарь из двух значений n=name1, a=age, у нас будет два ключа n и a
# с значениями "Nikita" и 8
name1 = "Nikita"
age = 8
tm1 = Template("I am {{ a }} years old and my name is {{ n }}")
msg1 = tm1.render(n=name1, a=age)
print(msg1)

# Можно выполнять любые конструкции языка Python
tm2 = Template("I am {{ a*2 }} years old and my name is {{ n.upper() }}.")
msg2 = tm2.render(n=name1, a=age)
print(msg2)

# ----------------------------------------------------------------------------
# Информация о человеке в виде класса Person
class Person():
   def __init__(self, name, age):
      self.name = name
      self.age = age

# создаем экземпляр этого класса Person  х
per = Person("Micke", 33)

# выведем информацию  с помощью шаблона, внутри скобок обращаемся к соответствующему
# свойству этого класса. Когда мы передаем в метод .render()p=per, то внутри шаблона это
# доступно по ссылке p. Обращаемся по этой ссылке p к соответствующему классу или просто к переменной
# или к коллекции какой-нибудь и т.д. Соответственно с этим объектом работаем
tm3 = Template("I am {{ p.age }} years old and my name is {{ p.name }}.")
msg3 = tm3.render(p=per)
print(msg3)

# ----------------------------------------------------------------------------
# Или например, внутрь класса Person(): пропишем два геттера
class Person1():
   def __init__(self, name, age):
      self.name = name
      self.age = age

# Первый геттер - взять имя
   def getName(self):
      return self.name
# Второй геттер - взять возраст
   def getAge(self):
      return self.age

per1 = Person1("Saymon", 20)

# Внутри шаблона воспользуемся геттерами getAge() и getName()
tm4 = Template("I am {{ p.getAge() }} years old and my name is {{ p.getName() }}.")
msg4 = tm4.render(p=per1)
print(msg4)

# ----------------------------------------------------------------------------
# Например, можно передать данные в шаблон с помощью словаря. 
per2 = {'name': 'Alex', 'age': 41}

# Передадим данные из словаря в шаблон, прописываем ключи нашего словаря
tm5 = Template("I am {{ p.age }} years old and my name is {{ p.name }}.")
msg5 = tm5.render(p=per2)
print(msg5)

# ----------------------------------------------------------------------------
# Например, можно передать данные в шаблон с помощью словаря. 
per3 = {'name': 'Bob', 'age': 25}

# Обратимся к ключу используя синтаксис - строка имя этого ключа
tm6 = Template("I am {{ p['age'] }} years old and my name is {{ p['name'] }}.")
msg6 = tm6.render(p=per3)
print(msg6)


