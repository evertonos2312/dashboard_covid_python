import os


class Config():
    CSRF_ENABLE = True
    SECRET = 'E93D26883C7D7EB1E5A93BA6CA51EF2EB1108DD4A5D68600'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    FORT_HOST = 8080
    URL_MAIN = 'http://%s/%s' % (IP_HOST, FORT_HOST)  # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva:de_m7jbG^wZ=@localhost:3306/dashboard_covid'


class TestingConfig(Config):
    pass


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'
