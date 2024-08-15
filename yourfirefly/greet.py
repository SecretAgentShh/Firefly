from flask import Flask, jsonify
import json

myapp = Flask(__name__)

@myapp.route('/')
def homepage():
  return jsonify({"message": "Hello, My Friend"})

if __name__ == '__main__':
  myapp.run(host='0.0.0.0', port=80)