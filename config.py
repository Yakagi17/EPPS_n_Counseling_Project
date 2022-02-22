import json

with open("secret.json") as config_file:
    config_data = json.load(config_file)


class Config(object):
    SECRET_KEY = config_data["flask_secret_key"]
    SQLALCHEMY_DATABASE_URI = f'{config_data["database"]["dbms"]}\
        ://{config_data["database"]["user"]}\
        :{config_data["database"]["password"]}\
        @{config_data["database"]["host"]}\
        /{config_data["database"]["database_name"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
