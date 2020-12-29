from os import environ
from flask import Flask, make_response
from flask_restful import Resource, Api
from waitress import serve
import sqlite3
import sys

app = Flask(__name__)
api = Api(app)

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

class Config():
  port = environ.get('PORT') or 8080

class Employees(Resource):
  def get(self):
    try:
			# Note: there are more efficient approaches for
			# transacting with a db than opening/closing a new connection
			# on each request. For example, using a connection pool
			# typically provides better scalability.
			# However, if scalability is a concern then we probably
			# want to use something other than SQLite anyway.
      dbConnection = sqlite3.connect('db/employees.db')
      dbConnection.row_factory = dict_factory
      c = dbConnection.cursor()
      data = c.execute('select * from employees').fetchall()
      dbConnection.close()
      return data
    except:
      print("Caught error:", sys.exc_info()[0])
      raise
  pass

api.add_resource(Employees, '/employees')

@app.route("/")
def home():
  headers = {"Content-Type": "application/json"}
  return make_response(
    'Welcome!',
    200,
    {"Content-Type": "application/json"}
  )

if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=Config.port)
