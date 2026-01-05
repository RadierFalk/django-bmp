# Django BMP

Sistema financeiro multi-tenant desenvolvido com Django.

## 🚀 Tecnologias
- Python
- Django
- Django REST Framework
- SQLite / PostgreSQL
- Tailwind CSS

## ⚙️ Como rodar o projeto

```bash
git clone https://github.com/RadierFalk/django-bmp.git
cd django-bmp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
