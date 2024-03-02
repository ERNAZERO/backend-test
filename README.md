Для начала установите все зависимости:
```bash
pip install -r requirements.txt
```

Создайте нужные таблицы при помощи команд:
```
python manage.py makemigrations user
python manage.py migrate
python manage.py makemigrations post       
python manage.py migrate
```

Для бд я использовал PostgreSQL, в settings.py настроил так:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}
```

Для удобства работы с API использовал Postman. 

Логин для получения токена:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 48 01" src="https://github.com/ERNAZERO/backend-test/assets/45794773/5cc01032-989e-413c-9a85-b1ae683f83e5">


Регистрация:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 53 40" src="https://github.com/ERNAZERO/backend-test/assets/45794773/968aadfc-9372-4930-b702-62350491b651">


Список постов с пагинацией и счетчиком постов. На одной странице максимально может быть только 5 постов.
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 48 57" src="https://github.com/ERNAZERO/backend-test/assets/45794773/9aa4d2b0-8c33-404b-ba87-d206c9e07d5e">


Добавление поста:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 50 35" src="https://github.com/ERNAZERO/backend-test/assets/45794773/fb78d9c8-5d1c-49f1-b1e5-040fc2abfaa0">


Добавление комментария к посту:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 52 45" src="https://github.com/ERNAZERO/backend-test/assets/45794773/82988999-db02-42ed-bec8-306f486a538e">


Просмотр конкретного поста с его комментариями:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 51 33" src="https://github.com/ERNAZERO/backend-test/assets/45794773/1bdccf6f-fb0d-403a-80b8-c704b3a8295c">


Лайк:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 51 47" src="https://github.com/ERNAZERO/backend-test/assets/45794773/70bad1f9-ef53-4912-8ae7-59bf30644b9d">


При повторном отправлении запроса лайка, лайк убирается:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 52 16" src="https://github.com/ERNAZERO/backend-test/assets/45794773/71f566ef-984b-4913-aa9a-835d6e7e8cf5">


