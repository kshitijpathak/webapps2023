import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROD = False
SQLITE = True
AWS = False

def get_database():
    if SQLITE:
        return {
            'ENGINE': "django.db.backends.sqlite3",
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    else:
        # CREATE PROD VERSION DATABASE FOR DEPLOYMENT
        if PROD:
            return {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'webapps2023',
                'USER': 'postgres',
                'PASSWORD': '9910824140',
                'HOST': 'webapps2023.cxafw8hsfido.us-east-1.rds.amazonaws.com',
                'PORT': '5432',
            }
        elif AWS:
            return {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'webapps2023',
                'USER': 'postgres',
                'PASSWORD': '9910824140',
                'HOST': 'webapps2023.cxafw8hsfido.us-east-1.rds.amazonaws.com',
                'PORT': '5432',
            }
        else:
            return {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'webapps2023',
                'USER': 'postgres',
                'PASSWORD': '9910824140',
                'HOST': 'localhost',
                'PORT': '5432',
            }