from .base import *
import dj_database_url
import environ
import cloudinary.uploader
import cloudinary.api
import cloudinary


env = environ.Env(
    DEBUB=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["themirrored-production.up.railway.app", "themirrored.com"]

cloudinary.config( 
  cloud_name = "damdz7xux", 
  api_key = env('CLOUDINARY_API_KEY'), 
  api_secret = env('CLOUDINARY_SECRET')
)

DATABASES = {
    "default": dj_database_url.config(default='postgresql://postgres:ASsEPX7RNV5JPN3RkOzu@containers-us-west-137.railway.app:6528/railway', conn_max_age=1800),
}

EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')




try:
    from .local import *
except ImportError:
    pass
