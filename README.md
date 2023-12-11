1) Создаем миграции базы данных:
   ```
   python manage.py makemigrations
   ```
2) Применяем миграции базы данных:
   ```
   python manage.py migrate
   ```
3) Создаем тестовые данные:
   ```
   python manage.py loaddata fixtures.json
   ```
4) Создаем супер-пользователя:
   ```
   python manage.py createsuperuser
   ```
5) Запускаем Сервер приложения:
   ```
   python manage.py runserver
   ```
6) Переходим по ссылке в браузере:
   127.0.0.1:8000
   
