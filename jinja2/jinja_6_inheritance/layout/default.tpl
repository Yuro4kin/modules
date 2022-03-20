<!-- # Подкаталог layout берется относительно текущего подшаблона 'layout/default.tpl' -->
<!-- Представляет такой же шаблон с которм только-что работали как ex_main.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- # Новый тип блоков - именованный блок с именем title -->
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

<!-- # Новый тип блоков - именованный блок с именем title -->
<!-- % block content % -->
<!--{                 }-->
Block content - super

<!-- # В шаблонах можно делать вложенные блоки -->
    {% block content %}
         {% block table_contents %}
         <ul>
         {% for li in list_table -%}
         <li>{% block item scoped%}{{ li }}{% endblock %}</li>
         {% endfor -%}
         </ul>
         {% endblock table_contents %}
    {% endblock content %}


<!--% endblock %-->
<!--{           }-->

</body>
</html>