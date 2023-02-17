# Инструкция по развертыванию

1. Создать виртуальное окружение
`python3 -m venv venv_name`
2. `source venv_name/bin/activate` - активируем окружение
3. `pip install -r requirments.txt` - устанавливаем библиотеки
4. `python manage.py migrate`
5. `python manage.py runserver`

## запуск терминала в контексте джанго
`python manage.py shell_plus --ipython

### сохранение списка библиотек окружения
`pip freeze > requirements.txt`

### fixtures
`python manage.py dumpdata MainApp > MainApp/fixtures/save_all.json`


## выполненные задания
###Задания 
### Выполнять после: Модуль-1
1.	Создайте новый проект DjangoCountries. 
Создайте новое виртуальное окружение(venv), установите в него Django.
Рекомендация: выполните все действия используя терминал Linux.
2.	Главная страница должна быть доступна по корневому url’у.
На ней разместите произвольное приветствие c минимальным HTML оформлением.
3.	Запустите проект и проверьте отображение главной страницы.
4.	Загрузите ваш проект на GitHub
Важно: не забудьте в проект добавить .gitignore. Виртуальное окружение и настройки вашей IDE не должны быть частью репозитория.
### Выполнять после: Модуль-2
5.	Оформите главную страницу в виде полноценного html-документа
6.	Список с данными для стран возьмите тут.
Примечание: пока мы работаем без БД, скопируйте данные о странах в файл (разместите файл в корне проекта).
 Для получение информации из файла используйте работу с файлами в Python, работа с json-1 и работа с json-2.
7.	По url: /countries-list/ отобразите нумерованный список всех стран, отобразив в списке только названия стран.
8.	Название каждой страны сделайте гиперссылкой, которая ведет на персональную страницу данной страны. 
На персональной странице страны отобразите ее название(в виде заголовка) и список всех языков, на которых говорят в данной стране.
9.	На главной странице добавьте еще одну ссылку “Языки”. По ссылке отобразите страницу со списком всех языков на котором говорят во всех странах.
### Выполнять после: Модуль-3
10.	Создайте модель-класс Country.
11.	Перенесите все страны из исходного json файла в базу данных(БД).
12.	Измените работу вашего приложения на работу с БД
13.	Выгрузите данные из БД в фикстуру(fixture) countries.json

### Выполнять после: Модуль-4
14.	Используя информацию с занятия, измените структуру БД, реализовав связь “многие-ко-многом” для стран и языков.
Не забудьте: выгрузить обновленные данные из БД fixture: countries.json
15.	Добавьте в проект файл requirements.txt
16.	Добавьте в проект файл README.md, добавив в него:
○	Информацию о запуске проекта после клонирования
○	Список всех заданий, пометив выполненные