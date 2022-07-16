# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x7=q1++p5i5hyympo_^4g(-i3mn1$d-+q_lud=9+6c$5r6(lk!'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}