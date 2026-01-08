 # Django ORM Template (Library)


 Це простий шаблон-додаток Django для  роботи з ORM складних запитів 
 Моделі 
 - `Author`
 - `Publisher`
 - `Book`
 - `Genre`

 **Quick start**

 - **Клонування з GitHub**:

 ```bash
 git clone < git@github.com:GoIteensCources/WEB_61_Django_orm_template.git >
 cd ORM_template
 ```


 **Встановлення та запуск**
 ---------------

 1. Створіть і активуйте віртуальне середовище:

 ```bash
 python3 -m venv venv
 source venv/bin/activate
 ```

 2. Встановіть залежності:

 ```bash
 pip install -r requirements.txt
 ```

 3. Застосуйте міграції:

 ```bash
 python3 manage.py migrate
 ```

 4. (Опціонально) Створіть адміністратора Django:

 ```bash
 python3 manage.py createsuperuser
 ```

 5. Наповніть базу даних прикладами (seed):

 ```bash
 python3 manage.py seed_library --books 5000
 ```

 6. Запустіть сервер розробки:

 ```bash
 python3 manage.py runserver
 ```

 **Додавання записів у базу**
 ---------------

 1) Через адмінку

 - Перейдіть на `http://127.0.0.1:8000/admin/`, увійдіть під створеним суперкористувачем і додайте `Author`, `Publisher`, `Genre` та `Book` через інтерфейс.

 2) Через Django shell (приклад)

 ```bash
 python3 manage.py shell
 ```

 У інтерактивному шеллі виконайте наступне:

 ```python
 from library.models import Author, Publisher, Genre, Book

 # Створити автора
 a = Author.objects.create(first_name='Ivan', last_name='Franko', country='Ukraine', birth_year=1856)

 # Створити видавництво
 p = Publisher.objects.create(name='Example Pub', city='Kyiv', established_year=1990)

 # Створити жанр
 g = Genre.objects.create(name='Fiction')

 # Створити книгу та додати жанр
 b = Book.objects.create(title='My Book', publication_year=2020, pages=300, price='199.99', author=a, publisher=p)
 b.genres.add(g)
 b.save()

 # Перевірити
 print(Book.objects.all())
 ```

 3) Використати скрипт seed

 - Запустіть `python3 manage.py seed_library` — команда автоматично додає прикладові записи (якщо в проєкті реалізовано відповідну management-команду).
