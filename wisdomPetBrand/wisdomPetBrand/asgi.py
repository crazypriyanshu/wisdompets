"""
ASGI config for wisdomPetBrand project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
# Provides hooks for the web servers apache or nginx
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wisdomPetBrand.settings')

application = get_asgi_application()
