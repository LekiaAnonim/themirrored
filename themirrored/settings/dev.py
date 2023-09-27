from .base import *
import cloudinary.uploader
import cloudinary.api
import cloudinary
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-2^5dhj0b%0ca-s(@wksf7^-ml+lvbkho0_3dlx-6cah8x@mgqg"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_HOST_USER = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

cloudinary.config( 
  cloud_name = "damdz7xux", 
  api_key = os.getenv('CLOUDINARY_API_KEY'), 
  api_secret = os.getenv('CLOUDINARY_SECRET')
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

# DATABASES = {
#     "default": dj_database_url.config(default='postgresql://postgres:ASsEPX7RNV5JPN3RkOzu@containers-us-west-137.railway.app:6528/railway', conn_max_age=1800),
# }


try:
    from .local import *
except ImportError:
    pass
