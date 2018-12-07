# ElMuro

> Responsive meme page with hot, new and top ranking based in reddit hot algorithm

![](elmuro.gif)

Check the live version at:
https://www.elmuro.pw/

### Dependencies

Python 3
Pip 

### Install

install python3

```
$ sudo apt install python3
```

install pip

```
$ sudo apt-get install python-pip python-dev build-essential 
```

clone repository

```
$ git clone (url)
```

create a local virtual enviroment

```
$ virtualenv env
```

activate env

```
$ source env/bin/activate
```

install requirements

```
$ env/bin/pip install -r requirements.txt 
```

Debug and run backend server
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Other commands see
https://docs.djangoproject.com/en/2.0/

## Deploy

Use gunicorn and nginx for the backend

## Built With

* [Django](https://www.djangoproject.com/) - Web Framework
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Bootstrap](https://getbootstrap.com/) - CSS Framework

## Authors

* **Emmanuel Perez** - *Initial work* - [EmmanuelPerezP](https://github.com/EmmanuelPerezP)
Twitter: [@EmmanuelPdev](https://twitter.com/EmmanuelPdev)

