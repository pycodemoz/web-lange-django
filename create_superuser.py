import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.contrib.auth.models import User

# Altere estas credenciais
username = 'flange'
email = 'riolange86@gmail.com'
password = 'Riqueza1822'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superusuário {username} criado com sucesso!')
else:
    print(f'Usuário {username} já existe.')