from .base import *
import dj_database_url
import environ
import cloudinary.uploader
import cloudinary.api
import cloudinary


env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["themirrored-production.up.railway.app", "www.themirrored.com", "themirrored.com"]

cloudinary.config( 
  cloud_name = "damdz7xux", 
  api_key = "365139568314788", 
  api_secret = "m2OEjq0TA6lSOWmsmEvlyGoFGzg"
)

DATABASES = {
    "default": dj_database_url.config(default='postgresql://postgres:3DDF4Cce6E556D4BBG22b6bD1dda3ECA@viaduct.proxy.rlwy.net:33148/railway', conn_max_age=1800),
}

EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# WAGTAIL ANALYTICS SETUP
GA_KEY_CONTENT = env('GA_KEY_CONTENT')
GA_VIEW_ID = env('GA_VIEW_ID')


try:
    from .local import *
except ImportError:
    pass
