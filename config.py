import os


class Config():
    CSRF_ENABLE = True
    SECRET = 'E93D26883C7D7EB1E5A93BA6CA51EF2EB1108DD4A5D68600'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None
