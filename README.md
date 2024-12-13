Если кому-то захочется запустить проект, для начала вам нужно будет установить язык программирования python (https://www.python.org/), и выполнить следующие шаги алгоритма:

1. создаете и открываете папку в своем редакторе кода

2. вводите команду git clone 'ссылка на репозиторий'

3. открываете консоль(или командную строку) и находясь в директории проекта(внутри только что созданной папки), вводите команду 'python -m venv venv' если на windows, или 'python3 -m venv venv' если на линуксовых системах

4. Далее, в консоли, находясь в одной директории с созданной папкой 'venv' вводите команду: если на windows - venv\Scripts\activate, если на линуксе - загуглите, не помню(гуглите как активировать виртуальное окружение python)

5. теперь переходите во внутрь директории проекта(туда где лежит файл requirements.txt, manage.py и тд) и вводите команду pip install requirements.txt

6. После, вводите две команды: python manage.py makemigrations и python manage.py migrate, если не вылезло никаких ошибок, переходите к следующему шагу

7. Теперь вводите команду python manage.py runserver и переходите по адресу, который вывелся в консоль(http://localhost:8000/)

8. ЧТобы добавить вопросы, или ответы вам нужно будет создать супер-пользователя командой python manage.py createsuperuser, и перейти по адресу http://localhost:8000/admin/

9. Логика опросника следующая: вы сначала добавляете вопрос(Question), определяете его порядкой номер, затем добавляете ответ(Answer), указываете на какой вопрос Answer отвечает, и следующий вопрос, на который перенаправит абитуриента после выбора данного ответа.