# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Import module models (i.e. Doctor)
from app.doctor.models import Doctor

#Import module service
from app.doctor.service import *



# Define the blueprint: 'doctor', set its url prefix: app.url/doctor
mod_doc = Blueprint('doctor', __name__, url_prefix='/doctor')

@mod_doc.route('/get-doc-by-id', methods=['GET', 'POST'])
def get_doc_by_id():
    return "Doctor Returns"

@mod_doc.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello {}!".format(name)