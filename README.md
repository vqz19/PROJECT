# Secret manager project

#### Gestor de contraseñas, el cual cuenta con funcionalidades como almacenarlas, crearlas, exportalas, importarlas, etc...

## step creation project (0-step)

Create a virtual enviroment

~~~
python -m venv venv
~~~

Activate virtual enviroment

~~~
source venv/Scripts/activate
~~~


install python dependencies

~~~
pip install -r requirements.txt
~~~

## Execute program

~~~
flask --app secret_manager.app run --debug
~~~