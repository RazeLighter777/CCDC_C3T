#!/usr/bin/env python3

######## Imports ########
from flask import Flask, request
import json, os, sys, hashlib, time, socket

######## Global Variables #########
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
path = "/var/log/httppot.log"

app = Flask(__name__)
methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"]

@app.route('/', defaults={'path': ''},  methods = methods)
@app.route('/<path:path>',  methods = methods)
def all_routes(path):
  dict = defaultActions(request)
  write(dict)
  return ''

def defaultActions(request):
  dict = {}
  dict = parseHeaders(request.headers, dict)
  dict['request_type'] = request.method
  dict['path'] = request.full_path
  dict['ip_address'] = request.remote_addr
  dict['port'] = PORT
  if request.method == 'POST':
    dict['body'] = request.get_data().decode('utf-8')
  dict['hash'] = hashlib.md5(json.dumps(dict).encode('utf-8')).hexdigest()
  dict['unix_timestamp'] = int(time.time())
  dict['readable_timestamp'] = time.ctime()
  return dict


def parseHeaders(headers, dict):
  for header in headers:
    dict[header[0]] = header[1]
  return dict

def write(logline):
  with open(path, "a") as file:
    file.write(json.dumps(logline))
    file.write("\r\n")

if __name__ == "__main__":
  app.run(host=HOST, port=PORT, debug=True)