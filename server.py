from flask import Flask

srv = Flask(__name__)

@srv.route("/")
def home():
  return "<h1>it works</h1>"

@srv.route("/api/ls")
def ls():
  return {
    'os': 'gnu/linux',
    'ram': 8
  }
