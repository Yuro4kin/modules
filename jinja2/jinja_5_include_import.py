# Jinja2 #5: Конструкции include и import
from jinja2 import Environment, FileSystemLoader, FunctionLoader

# Исходный шаблон страницы делится на три части
# header content footer
#  file   file    file
# Construction include

# Разобьем страницу main_include.html на три составляющие page.html, header.html, footer.html

persons = [
    {"name": "Alex", "old": 19, "weight": 78.5},
    {"name": "Nick", "old": 29, "weight": 82.3},
    {"name": "Ivan", "old": 34, "weight": 94.0}
]

file_loader = FileSystemLoader('jinja_5_include_import')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain="https://flaskexamp1.herokuapp.com/", title="Website about Jinja")
# два именованных параметра domain, title для файла header.html
 
print(msg)

# Через блок include подключаются heder.html, footer.html в остальные .html страницы
# Error - jinja2.exceptions.TemplateNotFound: header2.html - мы не нашли файл header2.html
# Мы можем проигнорировать файл в page.html если его нет {% include 'header2.html' ignore missing %}

# У каждой страницы свой заголовок в странице <title>
# Например нам нужно  header  подставлять свой заголовок для каждой страницы
# Теперь для каждой страницы можем написать собственный заголовок


# К блоку include - подключим сразу нескольких файлов 
# {% include['page1.html','page2.html'] ignore missing%}

# import - позволяет не только включать отдельные файлы в шаблон, но и импортировать их
# отличие import от include файл не добавляется, можем использовать функционал этого файла, кот. импортируем
# Часто это делается, когда в импортируемом файле находится макрос, и этот макрос мы используем в исходном шаблоне
