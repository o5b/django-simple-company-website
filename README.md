# English

For `Django >= 2.0` compatible with `Python >= 3.5`

## Structure

Recommend installation virtualenv in `.env` folder in project folder.

```
/.git
/.env         - virtualenv
/applications - folder for django applications
---/main      - start app point that I offer for you
/frontend     - folder for source "frontend" files
---/images    - gulp tasks look at this folder, files get->optimize->put to `/static/images/`
---/scripts   - gulp tasks look at this folder, files get->minify->put to `/static/scripts/`
---/styles    - gulp tasks look at this folder, get _common.styl->optimize->put to `/static/styles/base.css`
/requirements - requirements for current project
/settings     - django settings
/tasks        - gulp tasks
```

## Install

```
git clone https://github.com/o5b/django-simple-company-website.git
cd django-simple-company-website/
python3.7 -m venv .env
source .env/bin/activate
pip install -r requirements/base.txt
npm i
```

## Usage

### Server (one terminal tab)

```
python manage.py runserver localhost:8000
```

### Frontend (other terminal tab)

```
npm start
```

### The haystack problem

**Django 3** removed the **six** package from **django.utils** and this results in an error importing it into the **haystack**. There are several ways to fix this.

1) Install **six** in virtual environment:

```
pip install six
```

in the **haystack** package change, where necessary, import from:

```
from django.utils import six
```

to

```
import six
```

2)In order not to change the line with the import of the **six** package, you can add the **six** package file yourself (for example, by copying `.env/lib/python3.7/site-packages/six.py`) to **django.utils** (`.env/lib/python3.7/site-packages/django/utils/`)

We also fix the import line in the file

```
.env/lib/python3.7/site-packages/haystack/inputs.py
```

instead

```
from django.utils.encoding import force_text, python_2_unicode_compatible
```

add

```
from django.utils.encoding import force_text
from six import python_2_unicode_compatible
```

### Database migrations and superuser creation

```
python manage.py migrate
python manage.py createsuperuser
```

### Django-modeltranslation

#### Synchronizing Model Fields

```
python manage.py sync_translation_fields
```

#### If you need to transfer the data that was originally in the model to the fields created by django-modeltranslation

```
python manage.py update_translation_fields
```

### Add test data to the database

```
python manage.py loaddata fixtures/db.json
```

#### If you need to save data from the database to fixtures

```
python manage.py dumpdata capture main services --indent 2 > fixtures/db.json
```

### If you need to do indexing for haystack

```
python manage.py rebuild_index
```

or

```
python manage.py update_index
```

### Celery is used to perform asynchronous tasks

**Redis** is used as a broker (must be installed and running).

Running **Celery**:

```
cd django-simple-company-website/
source .env/bin/activate
celery -A settings worker -l info
```

You can use **Flower** to monitor tasks:

```
cd django-simple-company-website/
source .env/bin/activate
celery -A settings flower
```

then open the page in the browser: `http://localhost:5555/`

# Russian

Для `Django >= 2.0` совместно с `Python >= 3.5`

## Структура

Рекомендуется устанавливать virtualenv в папку `.env` в папку проекта.

```
/.git
/.env         - папка для установки виртуального окружения
/applications - папка django applications
---/main      - основное приложение
/frontend     - папка для "фронтенд" файлов
---/images    - задачи gulp ищут в этой папке файлы, берут их->оптимизируют->помещают в `/static/images/`
---/scripts   - задачи gulp ищут в этой папке файлы, берут их->минимизируют->помещают в `/static/scripts/`
---/styles    - задачи gulp ищут в этой папке, берут _common.styl->оптимизируют->помещают в `/static/styles/base.css`
/requirements - зависимости для текущего проекта
/settings     - настройки django
/tasks        - gulp задачи
```

## Установка

    git clone https://github.com/o5b/django-simple-company-website.git
    cd django-simple-company-website/
    python3.7 -m venv .env
    source .env/bin/activate
    pip install -r requirements/base.txt
    npm i

## Использование

### Сервер (в консоли терминала)

```
python manage.py runserver localhost:8000
```

### Фронтенд (в другой консоли терминала)

```
npm start
```

### Проблема с haystack

В **Django 3** удалили пакет **six** из **django.utils** и это приводит к ошибке при его импорте в **haystack**. Исправить это можно несколькими способами.

1) Установить **six** в виртуальное окружение:

```
pip install six
```

а в пакете **haystack** изменить, где надо, импорт с:

```
from django.utils import six
```

на

```
import six
```

2)Чтобы не менять строку с импортом пакета **six** можно самостоятельно добавить файл пакета **six** (например скопировав `.env/lib/python3.7/site-packages/six.py`)  в **django.utils** (`.env/lib/python3.7/site-packages/django/utils/`)

Также исправляем строку с импортом, в файле

```
.env/lib/python3.7/site-packages/haystack/inputs.py
```

вместо

```
from django.utils.encoding import force_text, python_2_unicode_compatible
```

добвляем

```
from django.utils.encoding import force_text
from six import python_2_unicode_compatible
```

### Миграции для базы данных и создание суперпользователя

```
python manage.py migrate
python manage.py createsuperuser
```

### Django-modeltranslation

#### Синхронизируем поля модели

```
python manage.py sync_translation_fields
```

#### Если нужно перенести данные, которые были в модели изначально, в поля созданные django-modeltranslation

```
python manage.py update_translation_fields
```

### Наполнить бд тестывыми данными

```
python manage.py loaddata fixtures/db.json
```

#### Если нужно сохранить данные из бд в fixtures

```
python manage.py dumpdata capture main services --indent 2 > fixtures/db.json
```

### Если необходимо сделать индексирование для haystack

```
python manage.py rebuild_index
```

или

```
python manage.py update_index
```

### Celery - для выполнения асинхронных задач

В качестве брокера используется **Redis** (должна быть установленна и запущена). Запуск **Celery**:

```
cd django-simple-company-website/
source .env/bin/activate
celery -A settings worker -l info
```

Для мониторинга можно использовать **Flower**:

```
cd django-simple-company-website/
source .env/bin/activate
celery -A settings flower
```

затем открываем в браузере: `http://localhost:5555/`
