# construtora
Projeto que permite CRUD de engenheiros, materiais de construção e projetos de construção.

Os projetos têm engenheiro responsavel e lista de materiais previamente cadastrados. 
O orçamento subtotal do projeto é calculado automaticamente.

Utilizando Django e Bootstra.

Instruções para instalar:
Ambiente virtual: 
python -m venv venv
venv\Scripts\Activate
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
