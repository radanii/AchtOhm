import os
from sqla_wrapper import SQLAlchemy

# db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))

# USE THIS TO CONNECT TO HEROKU DATABASE
db = SQLAlchemy(os.getenv("DATABASE_URL",
                          "postgres://vbnuczkqpdmuaw:9f7036a79d94b51e3fedc899ca6e77b387f6b3ed4707d63e082d410e21d86afa@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/d26b2unj72ae4a"))
#
#
# Implementation of config to use both at the same time will be happening with the manage.py


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    message = db.Column(db.String)
    bool_message = db.Column(db.String)
    password = db.Column(db.String)
    session_token = db.Column(db.String)

