from flask import Flask, jsonify, make_response, request, render_template, Response, session, redirect, copy_current_request_context
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

app = Flask(__name__,template_folder='../views',static_folder='../static')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


load_dotenv()

PATH_API = os.getenv('PATH_API')

