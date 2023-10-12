from flask import Flask, request, Response
import socket
import json


app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Fibonacci Server'


@app.route('/register', methods = ['PUT'])
def register():
    data = request.json
    hostname = data.get('hostname')
    fs_ip = data.get('fs_ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')
    as_rq = {'NAME': hostname, 'TYPE': 'A','VALUE':fs_ip,'TTL':10}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.sendto(json.dumps(as_rq).encode(), (as_ip, int(as_port)))
        data = s.recv(1024)
    data = data.decode()
    return data

@app.route('/fibonacci',methods = ['GET'])
def fabonacci():
    x = request.args.get('number')
    f = int(x)
    fab = calculation(int(x))
    return Response(str(fab), status=200)

def calculation(f):
    if f <= 1:
        return f
    else:
        return calculation(f - 1) + calculation(f - 2)

app.run(host='0.0.0.0',
        port=9090,
        debug=True)