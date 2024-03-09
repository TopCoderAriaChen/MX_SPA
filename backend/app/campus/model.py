from flask_mongoengine import Document
from mongoengine import StringField


class Campus(Document):
    name = StringField(required=True, max_length=200)
