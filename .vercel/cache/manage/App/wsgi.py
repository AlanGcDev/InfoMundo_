import os
import sys
from django.core.wsgi import get_wsgi_application

# Establece las configuraciones del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Exponer la aplicación como `app` para que Vercel la detecte
app = get_wsgi_application()  # Este es el handler que Vercel busca

# Lógica para ejecutar comandos de gestión de Django
if __name__ == '__main__':
    try:
        execute_from_command_line = __import__('django.core.management').core.management.execute_from_command_line
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error ejecutando el servidor: {e}")
