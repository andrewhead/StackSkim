from datetime import date
from peewee import *


db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.


db.connect()
db.create_tables([Person], safe=True)

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
uncle_bob.save() # bob is now stored in the database
uncle_bob = Person.select().where(Person.name == 'Bob').get()
print uncle_bob.birthday
