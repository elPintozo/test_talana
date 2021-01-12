# Talana
Prueba técnica

# Para correr el proyecto usando Python 3.7.1:

- $ git clone https://github.com/elPintozo/test_talana.git
- $ python manage.py pip install -r requirements.txt
- $ python manage.py makemigrations
- $ python manage.py migrate
    
y finalmente

- $ python manage.py runserver

## Si no se cuenta con la versión en particular de Python, o la local presenta errores se puede instalar Pyenv y luego:
- pyenv install 3.7.1
- pyenv virtualenv 3.7.1 entorno_talana
- pyenv activate entorno_talana

# Funciones ok
- El usuario se inscribe
- Debe registrar sus datos personales
- Si el email ya está inscrito, no te debe dejar volver a registrar a la persona
- Busca e indica en pantalla el ganador de haber uno

# Funciones pendientes

- Para activar el registro, la persona debe verificar su e-mail.
- Debes entregar un endpoint que gatille el sorteo y entregue un ganador


