from flask import Flask, jsonify, make_response, request, render_template, Response, session, redirect, copy_current_request_context

app = Flask(__name__,template_folder='../views',static_folder='../static')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

