# Django site

For `Django >= 2.0` compatible with `Python >= 3.5`

## Structure

Recommend installation virtualenv in `.env` folder in project folder.

```
/.git
/.env	      - virtualenv
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

    git clone https://github.com/o5b/django-simple-company-website.git
    cd django-simple-company-website/
    python3.7 -m venv .env
    source .env/bin/activate
    pip install -r requirements/base.txt
	npm i

## Usage

### Server (one terminal tab)
	python manage.py runserver localhost:8000

### Frontend (other terminal tab)
	npm start

### Проблема с haystack

В Django 3 удалили пакет six из django.utils и это приводить к ошибке при его импорте в haystack. Исправить это можно несколькими способами.

1) Установить `six` в виртуальное окружение:
```
pip install six
```
а в пакете haystack изменить, где надо, импорт с:
```
from django.utils import six
```
на
```
import six
```

2)Чтобы не менять строку с импортом пакета `six` можно самостоятельно добавить файл пакета six (например скопировав `.env/lib/python3.7/site-packages/six.py`)  в django.utils (`.env/lib/python3.7/site-packages/django/utils/`)

Также в файле
```
.env/lib/python3.7/site-packages/haystack/inputs.py
```
исправляем строку с импортом, вместо
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

### django-modeltranslation

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

`python manage.py rebuild_index` или `python manage.py update_index`

