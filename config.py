import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True

    FLASK_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASK_MAIL_SENDER='Fasky Admin <flasky@example.com>'
    FLASK_ADMIN=os.environ.get('FLASK_ADMIN') or 'admin'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or 'h@google.com'
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') or 'password'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL') or 'mysql://root:pass@localhost/develop'

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or 'mysql://root:pass@localhost/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'mysql://root:test@192.168.1.102/test'

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':ProductionConfig

}
