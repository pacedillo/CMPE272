import datetime
from .order import Order
from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField


class Customer(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    address = StringField(required=True, max_length=200)
    email = StringField(required=True, max_length=50)
    phone = StringField(default=datetime.datetime.now)
    customer_since = DateTimeField(default=datetime.datetime.utcnow())
    orders = ListField(ReferenceField(Order))

