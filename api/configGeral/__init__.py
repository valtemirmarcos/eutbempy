from flask import Flask, jsonify, make_response, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy 
import mysql.connector
import json

app = Flask(__name__,template_folder='views')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://valtemir:123456@127.0.0.1/producao_130123'
dbConfig = SQLAlchemy(app)

def convertNumero(numero):
    intNumero = int(numero)
    if intNumero/1000 > 1:
        return  str(int(intNumero/1000))+' Mil'
    else:
        return numero