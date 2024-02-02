
# Python Django Assignment



## Installation


Clone the repository:
```bash
  https://github.com/AbyvargheseMandapathel/ttofl_task.git
```

    
## Packages
Navigate into the directory and install required Packages

```bash
cd ttofl
pip install -r requirements.txt
```
## Database migrations:
Apply Database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
## Run Server

Start the server

```bash
  python manage.py runserver
```


## endpoints

```bash
http://127.0.0.1:8000/login/
```

```bash
http://127.0.0.1:8000/signup/
```

```bash
http://127.0.0.1:8000/authors/
```

```bash
http://127.0.0.1:8000/authors/export-books/<int:pk>/
```
eg: use pk as 4 

```bash
http://127.0.0.1:8000/add-book/
```
```bash
http://127.0.0.1:8000/book/edit-book/<int:pk>/
```
note : use pk as 4

```bash
http://127.0.0.1:8000/authors/
```
```bash
http://127.0.0.1:8000/genre/create/
```
```bash
http://127.0.0.1:8000/genre/<int:pk>/
```
```bash
http://127.0.0.1:8000/authors/<str:pk>//
```
eg: http://127.0.0.1:8000/authors/ARNEW0001/
```bash
http://127.0.0.1:8000/authors/ARNEW0001/books/
```

Note : Dont forget to add authorization tokens
Reference : https://youtu.be/AZfd6ecVoCg