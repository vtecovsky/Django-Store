# Django Store Server

## Features
<ul>
    <li>Authentication, authorization, registration</li>
    <li>Authentication via GitHub</li>
    <li>Sending emails for password confirmation</li>
    <li>Shopping cart</li>
    <li>Making an order</li>
    <li>Admin panel for moderators</li>
</ul>

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python -m venv <venv_name>
   <venv_name>\Scripts\activate.bat
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
    
    For Windows:
   ```bash
   python manage.py migrate
   python manage.py loaddata <path_to_fixture_files>
   python manage.py runserver 
   ```
   
4. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
   
5. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```
