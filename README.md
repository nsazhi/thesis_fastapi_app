# Blog — My Favorite Films
Интерактивный блог.

Создан в рамках дипломной работы по теме: «Анализ и сравнение написания web-приложений с использованием разных фреймворков».

## Цель проекта
Разработать простое веб-приложение с использованием FastAPI для сравнения с подобной разработкой на Flask и Django.

## Обзор проекта
Веб-приложение на базе фреймворка FastAPI, которое позволит:
* админстраторам вносить записи в базу данных;
* пользователям просматривать каталог полностью или фильтруя по категориям.

**Фронтенд:** Создан пользовательский интерфейс с использованием Jinja2 – для шаблонов, Bootstrap и CSS – для стилизации.
Для реализации страниц администрирования использованы формы.

**Бэкенд:** Реализована серверная логика с использованием фреймворка FastAPI.

Настроено подключение к СУБД: по умолчанию SQLite, но с возможностью быстрого подключения любой другой, указанной в файле `.env`.

Созданы модели для базы данных с помощью SQLAlchemy и валидации данных с помощью Pydantic.

Настроены миграции с помощью alembic.

Настроены маршруты для обработки запросов с помощью APIRouter.

Настроено хэширование паролей с помощью passlib.

Подключен модуль python-multipart для работы с формами.

## Структура проекта
Проект включает в себя следующие ключевые компоненты:

### Домашняя страница
Здесь отображается список всех категорий, имеющихся в базе данных. Каждый пункт — это ссылка на страницу каталога фильмов,содержащая slug категории в динамическом URL для фильтрации.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/main_page.jpg">

Рис. 1. Домашняя страница

### Страница каталога
Здесь отображаются карточки фильмов с информацией. В зависимости от параметров запроса, отображается весь каталог фильмов или с фильтрацией по категориям, а также меняется заголовок страницы.
Также на странице есть кнопка выбора фильтра со ссылками, содержащими параметры.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/catalog1.jpg">

Рис. 2. Страница полного каталога

#

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/catalog2.jpg">

Рис. 3. Страница каталога с отбором по категории при переходе с домашней страницы

#

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/catalog3.jpg">

Рис. 4. Страница каталога с отбором по категории из фильтра

#

### Панель администратора
Немаловажным для удобства внесения записей в базу данных является наличие панели администратора. FastAPI не предоставляет возможность автоматической генерации страниц администрирования, поэтому для их создания использованы формы.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/adm_log_fa.jpg">

Рис. 5. Авторизация админстратора

#

На странице добавления категории есть ссылка на страницу добавления фильма для удобства перемещения между панелями.
Поле `slug` не отображается в форме, а заполняется программно при внесении записи в базу данных.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/adm_cat_fa.jpg">

Рис. 6. Добавление категории

#

Поле `img_url`, на случай отсутствия ссылки, автоматически заполняется, загружая предустановленное изображение.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/adm_fil_fa.jpg">

Рис. 7. Добавление фильма

#

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/catalog4.jpg">

Рис. 8. Добавленный фильм с изображением по умолчанию

### СУБД (Database Management System)

Данный проект требует подключения СУБД для хранения данных. Он позволяет подключить любую СУБД, указанной в файле `.env`. Так как в перспективе возможно значительное увеличение объема данных, мной использовалась клиент-серверная реляционная СУБД PostgreSQL.

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/dms_adm_fa.jpg">

Рис. 9. Таблица администраторов в базе данных

#
<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/dms_cat_fa.jpg">

Рис. 10. Таблица категорий в базе данных

#
<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/dms_fil_fa.jpg">

Рис. 11. Таблица фильмов в базе данных

### Шаблоны страниц
base.html — базовый шаблон, подключающий Bootstrap и статические файлы. Содержит навигационную панель и футер. На его основе пишутся остальные шаблоны.

main.html — домашняя страница, отображающая все категории, имеющиеся в базе данных.

login.html — страница авторизации администратора.

cat_panel.html — страница добавления категории в базу данных.

film_panel.html — страница добавления фильма в базу данных.

films.html — страница каталога всех фильмов, имеющихся в базе данных. На ее основе пишется страница каталога отфильтрованных данных.

films_by_category.html — страница каталога фильмов с фильтром по категории из параметров запроса.

### Файловая структура проекта

<img src="https://github.com/nsazhi/thesis_fastapi_app/blob/master/screenshorts_fa/struc_fa.jpg">

## Установка проекта
