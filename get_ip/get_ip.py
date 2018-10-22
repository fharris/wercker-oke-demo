import json
import argparse

from bottle import Bottle, run, request

app = Bottle()


@app.route('/')
def get_ip():
    client_ip = request.environ.get('REMOTE_ADDR')
    return json.dumps({"client_ip": client_ip})

@app.route('/helloworld')
def helloworld():
    return json.dumps({"message": "Hola Mundo con Rest y Python para ACME!"})

@app.route('/mgg')
def mgg():
    return json.dumps({"message": "Python service response!!!! !!"})

@app.route('/xyz')
def xyz():
    return json.dumps({"message": "Python service response!!!! !!"})

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="HTTP API for returning a visitor's IP address.")

    parser.add_argument('hostname', default="0.0.0.0",
                        help='Host IP to listen on. ')

    parser.add_argument('port', default="8080", help='The port to listen on.')

    args = parser.parse_args()

    run(app, host=args.hostname, port=args.port)
