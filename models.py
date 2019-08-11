import os
from sqla_wrapper import sqlalchemy
from sqlalchemy import create_engine

db = create_engine("postgres://vbnuczkqpdmuaw:9f7036a79d94b51e3fedc899ca6e77b387f6b3ed4707d63e082d410e21d86afa@ec2-46-"
                   "137-91-216.eu-west-1.compute.amazonaws.com:5432/d26b2unj72ae4a")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    message = db.Column(db.String)

