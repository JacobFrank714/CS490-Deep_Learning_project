from flask import Blueprint, render_template, request
from pandas import read_csv
from .models import Prediciton

prediction = Blueprint('prediction', __name__)

@prediction.route('/', methods=['POST'])
def home():
    df = read_csv('prediction.csv')
  
    return render_template("prediction.html")