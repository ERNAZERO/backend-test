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
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 58 44" src="https://github.com/ERNAZERO/backend-test/assets/45794773/ce975063-8abd-4951-a618-92ebc8351747">

Регистрация:
<img width="1440" alt="Снимок экрана 2024-03-02 в 18 02 36" src="https://github.com/ERNAZERO/backend-test/assets/45794773/1b89b8e8-4a71-4727-b464-a0f0e524ce78">


Список постов с пагинацией и счетчиком постов. На одной странице максимально может быть только 5 постов.
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 48 31" src="https://github.com/ERNAZERO/backend-test/assets/45794773/17cfef67-8a61-4e96-97cf-40205b62baee">

Добавление поста:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 51 02" src="https://github.com/ERNAZERO/backend-test/assets/45794773/da47288a-1b27-4aea-8e48-107e7d08fb57">

Добавление комментария к посту:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 52 45" src="https://github.com/ERNAZERO/backend-test/assets/45794773/3bfcc7b8-66af-421c-82c4-8fe5d7a2ce8f">

Просмотр конкретного поста с его комментариями:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 53 39" src="https://github.com/ERNAZERO/backend-test/assets/45794773/216d4eb8-731a-4bb3-9e71-04c368c81a3f">

Лайк:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 56 00" src="https://github.com/ERNAZERO/backend-test/assets/45794773/70a30333-24c6-471e-b5b2-17045bd69e55">

При повторном отправлении запроса лайка, лайк убирается:
<img width="1440" alt="Снимок экрана 2024-03-02 в 17 57 02" src="https://github.com/ERNAZERO/backend-test/assets/45794773/47e1cf4d-7c2f-406a-95f3-5ba8e89d606d">
