import json
import urllib
import socket
import json
import sys
import os

HOST = 'server.com'
PORT = 9001

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error) as msg:
    print("[ERROR] %s\n" % msg.strerror, file=sys.stderr)
    sys.exit(1)

try:
    sock.connect((HOST, PORT))
except (socket.error) as msg:
    print("[ERROR] %s\n" % msg.strerror, file=sys.stderr)
    sys.exit(2)

line = {
    "message": "2016-08-24T19:21:44.865242Z laptop 52.3.221.36:35718 10.231.73.166:80 0.000039 0.00109 0.000022 301 301 0 349 \"GET http://endpoint.com:80/ HTTP/1.1\" \"check_http/v2.0.3 (nagios-plugins 2.0.3)\" - -\n",
    "type": "endpoint.com",
    "tags": [
        "beta",
        "lamda"
    ]
}


environment = 'laptop'
msg = line
out = json.dumps(msg).encode()
print(json.dumps(line))
sock.send(out)
sock.close()
