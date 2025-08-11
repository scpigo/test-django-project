# Тестовый Django-проект для обучения

Проект создан в учебных целях для изучения фреймворка Django

Проект представляет из себя набор API методов сервиса для заметок

## Установка
1. создать файл .env идентичный файлу .env.example
2. в корне проекта выполнить команду `docker-compose up -d --build`
3. применить миграции выполнив команду `python manage.py migrate`
4. создать администратора командой `python manage.py createsuperuser`
5. API методы доступны по адресу `http://localhost:7070/api/`
6. панель администратора доступна по адресу `http://localhost:7070/admin/`

## API методы
- /api/register (POST) - регистрация (username - логин, email - адрес электронной почты, password - пароль, password2 - подтверждение пароля)
- /api/login (POST) - авторизация (username - логин, password - пароль)
- /api/refresh (POST) - обновление JWT токена (refresh - refresh-токен)
- /api/notes (GET) - получить список заметок, созданных авторизированным пользователем
- /api/notes/<note_id> (GET) - получить заметку авторизированного пользователя по её Id
- /api/notes/create (POST) - создать заметку (title - заголовок, body - текст, parent_note - id родительской заметки (необяз.))
- /api/notes/<note_id>/delete (DELETE) - удалить заметку
- /api/notes/<note_id>/toggle (PATCH) - переключить статус заметки