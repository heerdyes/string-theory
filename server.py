from flask import Flask
from flask import request

srv = Flask(__name__)

@srv.route("/")
def home():
  return "<h1>welcome to the student information system</h1>"

@srv.route('/api/students', methods=['GET'])
def getstudents():
  return {'data': [], 'success': True, 'error': ''}

@srv.route('/api/addstudent', methods=['POST'])
def addstudent():
  print(request.get_json())
  return {'data': [], 'success': True, 'error': ''}

@srv.route('/api/delstudent/<int:stid>', methods=['DELETE'])
def delstudent(stid):
  print('deleting student: ' + stid)
  return {'data': [], 'success': True, 'error': ''}

@srv.route('/api/updstudent/<int:stid>', methods=['PUT'])
def updstudent(stid):
  print('updating student: ' + stid)
  print(request.get_json())
  return {'data': [], 'success': True, 'error': ''}

