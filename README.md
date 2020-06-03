# Task master 🌶️
Here is code for Python Flask, app called Taks Master, which allows user to do CRUD in db records. It's dynamically rendered with jinja2.

## Installing
please install all pip3 packets, and activate source
```
pip3 install flask, flask-sqlalchemy, jinja2
source my-env-/bin/activate
```
If there no test.db file, you need to create one

```
python3
>>>from app import db 
>>>db.create_all()

```
## Running 
run in console
```
python3 app.py
```
and then open  http://127.0.0.1:5000
*SHIFT+F5, if the styles not loaded properly