# Aula 17 - 14/02/2019
# Criação de api rest - django

# mkvirtualenv api-rest -p python
# pip install django
# pip install django-rest-framework
# pip list
# pip install markdown
# 
# https://www.django-rest-framework.org/#installation
# django-admin startproject nutricao
# cd nutricao
# python manage.py startapp paciente

# alterar o arquivo nutricao\settings.py
        # INSTALLED_APPS =
        # ,
        # 'paciente'

# entrar em Paciente\models.py, criar classe e atributos
# entrar na nutricao\urls.py
# python manage.py migrate
# python manage.py makemigrations

# python manage.py runserver

# python manage.py shell
# from paciente.models import Paciente
# Paciente.objects.create(nome='Ricardo', idade='1981-04-20 00:00:00', telefone='48512', profissao='Analista', email='rico@gmail.com')

# python manage.py createsuperuser
# python manage.py runserver

# pip install requests

# criar arquivo api_client.py
# escrever codigo para chamar a api criada



