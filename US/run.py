from flask import Flask, request, Response
import socket
import json
import requests

app = Flask(__name__)

@app.route("/")
def homepage():
    return "User Server"

@app.route("/fibonacci")
## The path accepts five parameters
def us():
    hostname = request.args['hostname']
    fs_port = request.args['fs_port']
    number = request.args['number']
    as_ip = request.args['as_ip']
    as_port = request.args['as_port']
    if not all([hostname, fs_port,number, as_ip, as_port]):
        return Response("Bad request", status = 400)
    ## get ip from as
    ip_rq = {'NAME': hostname, 'TYPE': 'A'}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.sendto(json.dumps(ip_rq).encode(), (as_ip, int(as_port)))
        data = s.recv(1024)
    data = data.decode()
    fs_ip = data.get("VALUE")

    response = requests.get(
        "http://"+fs_ip+":"+fs_port+"/fibonacci?number="+number)
    return response


app.run(host='0.0.0.0',
        port=8080,
        debug=True)