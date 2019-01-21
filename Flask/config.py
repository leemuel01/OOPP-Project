class Config:
    # Security stuff so no cookie configuration
    SECRET_KEY = '49dc263f9ebdbf0510c9273e5320e7df'

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    # Flask Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'medfriendemail@gmail.com'
    MAIL_PASSWORD = 'ooppmedfriend'
