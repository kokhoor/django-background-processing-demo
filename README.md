Background Processing in Django
===
Demo files for the talk I gave in #pyconmy2015
Slides can be accessed here: http://www.slideshare.net/kokhoor/background-processing-pycon-my-2015

Assumption(s):
You will setup your own virtual environment as necessary

How To:
---
1. Install requirements

    ```
    $ pip install -r docs/requirements.txt
    ```

2. To run the django web

    ```
    $ python manage.py runserver
    ```

    Note: If you're using a new database, you'll need to create the database and run schemamigration.

    ```
    $ python manage.py syncdb
    $ python manage.py migrate
    ```


3. To run the django-background-tasks worker

    ```
    $ python manage.py process_tasks
    ```

4. To run the django-rq worker(s):

    ```
    $ python manage.py rqworker default
    ```

    Note: You will need to run redis. Default is localhost port 6379

