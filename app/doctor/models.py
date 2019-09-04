# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

# Define a Doctor model


class Doctor(Base):

    __tablename__ = 'doctor_details'

    name = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False,
                      unique=True)
    contact = db.Column(db.String(20),  nullable=False)

    status = db.Column(db.SmallInteger, nullable=False)
    blood_group = db.Column(db.String(128),  nullable=True)
    degree = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, contact):

        self.name = name
        self.email = email
        self.contact = contact

    def __repr__(self):
        return '<Doctor %r>' % (self.name)
