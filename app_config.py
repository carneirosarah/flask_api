import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['DATABASE']['host']
port = int(config['DATABASE']['port'])
username = config['DATABASE']['username']
password = config['DATABASE']['password']
database = config['DATABASE']['database']

SQLALCHEMY_DATABASE_URI = f'postgresql://{username}:{password}@{host}:{port}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False