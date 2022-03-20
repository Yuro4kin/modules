# Jinja2 #4: Загрузчики шаблонов -  FileSystemLoader, PackageLoader, DictLoader, FunctionLoader
from jinja2 import Environment, FileSystemLoader, FunctionLoader


# Шаблоны хранятся в текстовых файлах и загружаются по мере необходимости
##link3 = '''<select name="cities">
##{% for c in cities %}
##    <option value="{{c['id']}}">{{c['city']}}</option>
##{% endfor %}
##</select>'''

# Environment - центральный объект, через который происходит работа с API данного пакета
# https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment
# предположим, что все наши шаблоны хранятся в подкаталоге
#                   templates
# также там находится файл main.htm со следующим содержимым:
##<!DOCTYPE html>
##<html>
##<head>
##         <base href="https://flaskexamp1.herokuapp.com/">
##         <title>About flask and codding</title>
##</head>
##<body>
## 
##<ul>
##{% for u in users -%}
##    <li>{{u.name}} 
##{% endfor -%}
##</ul>
## 
##</body>
##</html>

# Загрузим приложение, обработаем его, на выходе получим текстовую строку с содержимым из шаблона
# Для этого пропишем программу
# У нас есть список
persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Nick", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0}
]

# Воспользуемся загрузчиком, который представляет модуль - jinja - FileSystemLoader
# FileSystemLoader - работает с файловой системой нашего устройства, с жестким диском
# указываем из какого подкаталога мы будем брать наши шаблоны - 'templates'
# когда у нас загрузчик сформирован - file_loader, мы сделали экземпляр класса - FileSystemLoader() 
# на этот экземпляр класса - FileSystemLoader() ссылается file_loader,
# мы создаем еще один класс Environment() - через который происходит работа с API анного пакета
# в качестве параметров класс Environment() указываем loader 
# именованному параметру loader присваиваем ссылку file_loader на наш загрузчик
# т.е. загрузчик loader будет брать все наши шаблоны из подкаталога 'templates'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

# для начала возьмем шаблон main.html и вызовем метод get_template()
# который формирует экземпляр класса Template на основе содержимого main.html
# перенная tm будет ссылаться на экземпляр класса Template для которого вызываем render()
# метод render() для обработки нашего шаблона и получения на выходе текстовой строки преобразованного шаблона

tm = env.get_template('main.html')
msg = tm.render(users = persons)
 
print(msg)

# В нашем шаблоне {% for u in users -%} - users ссылается на person
# и у persons отображаем поле name в шаблоне {{u.name}}, т.е. имя соответствующего человека


# Помимо FileSystemLoader, который отвечает за загрузку шаблонов непосредственно из файловой системы,
# в Jinja есть еще несколько предопределенных загрузчиков:
# PackageLoader – для загрузки шаблонов из пакета(когда формируем модуль в виде пакета и из пакета берем шаблоны);
# DictLoader – для загрузки шаблонов из словаря;
# FunctionLoader – для загрузки на основе функции;
# PrefixLoader – загрузчик, использующий словарь для построения подкаталогов;
# ChoiceLoader – загрузчик, содержащий список других загрузчиков (если один не сработает, выбирается следующий);
# ModuleLoader – загрузчик для скомпилированных шаблонов.

# Например, FunctionLoader можно реализовать так
# Определим некую функцию, которая будет возвращать шаблон:
# (path) - это тот шаблон который хотим загрузить
# if - если этот шаблон принимает значение "index", то возвращаем строку '''Имя {{u.name}}, возраст {{u.old}}'''
# else - иначе возвращаем строку '''Данные: {{u}}'''
def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

# пропишем загрузчик FunctionLoader, передадим в качестве аргумента ссылку на функцию loadTpl
file_loader1 = FunctionLoader(loadTpl)
env1 = Environment(loader=file_loader1)

tm1 = env1.get_template('index2')
msg1 = tm1.render(u = persons[0])
# persons[0] - шаблон отображает только одно конкретное значение '''Имя {{u.name}}, возраст {{u.old}} '''
# u - в шаблоне используем ссылку u
print(msg1)
# мы взяли первый элемент нашей коллекции списка persons - "name": "Alex", "old": 18, "weight": 78.5
# и вывели информацию в соответствии с шаблоном
# если вместо index укажем index2 получим словарь {'name': 'Alex', 'old': 18, 'weight': 78.5}


# Документация - загрузки шаблоны из файловой системы
# https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.FileSystemLoader

