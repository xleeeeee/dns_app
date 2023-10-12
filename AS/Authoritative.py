from flask import Flask, request, Response
import json
import socket

app = Flask(__name__)
addr={}  ## store the value in somewhere persistent

#@app.route('/')
#def homepage():
 #   return "Authoritative Server"


@app.route('/')
def register():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind('0.0.0.0',53533)
    while True:
                        ## 1.check value exist
                        ## return value
                        ## store ip and port from register


app.run(host='0.0.0.0',
        port=53533,
        debug=True)