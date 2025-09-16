"""
Custom ORM Skeleton
Stage 1 – Python Internals & Data Model
"""

import sqlite3


class Field:
    """Descriptor for model fields."""
    def __init__(self, column_type="TEXT"):
        self.column_type = column_type
        self.name = None  # will be set by metaclass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # TODO: add validation if needed
        instance.__dict__[self.name] = value


class ModelMeta(type):
    """Metaclass for collecting fields and creating schema."""
    def __new__(mcs, name, bases, attrs):
        if name == "BaseModel":
            return super().__new__(mcs, name, bases, attrs)

        # collect fields
        fields = {
            k: v for k, v in attrs.items() if isinstance(v, Field)
        }
        attrs["_fields"] = fields

        cls = super().__new__(mcs, name, bases, attrs)

        # TODO: create SQL table for this model
        return cls


class BaseModel(metaclass=ModelMeta):
    """Base model for all ORM entities."""
    _connection = sqlite3.connect(":memory:")

    @classmethod
    def create_table(cls):
        # TODO: generate CREATE TABLE SQL from fields
        pass

    def save(self):
        # TODO: insert or update record
        pass

    @classmethod
    def all(cls):
        # TODO: fetch all rows
        pass


# Example usage (to implement after completing methods)
class User(BaseModel):
    id = Field("INTEGER")
    name = Field("TEXT")
    email = Field("TEXT")


if __name__ == "__main__":
    User.create_table()
    u = User()
    u.name = "Alice"
    u.email = "alice@example.com"
    u.save()

    print(User.all())
