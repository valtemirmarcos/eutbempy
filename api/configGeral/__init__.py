from flask import Flask, jsonify, make_response, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy 
import mysql.connector
import json
from flask_cors import CORS, cross_origin
import requests
import bcrypt
import datetime


app = Flask(__name__,template_folder='views')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://valtemir:123456@127.0.0.1/producao_130123'
dbConfig = SQLAlchemy(app)
# habilitar acesso total a api
CORS_ALLOW_ORIGIN="*,*" 
CORS_EXPOSE_HEADERS="*,*" 
CORS_ALLOW_HEADERS="content-type,*"
cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expor_headers= CORS_EXPOSE_HEADERS.split(","), support_credentials = True)

def convertNumero(numero):
    intNumero = int(numero)
    if intNumero/1000 > 1:
        return  str(int(intNumero/1000))+' Mil'
    else:
        return numero

def hoje():
    agora = datetime.datetime.now()
    return datetime.datetime.strftime(agora,"%Y-%m-%d %H:%M:%S")