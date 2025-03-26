import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

# Set the default settings module for the 'ecomm' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomm.settings')

# Get the WSGI application
application = get_wsgi_application()

# Use Waitress to serve the application
if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
