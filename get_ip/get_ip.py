import json
import argparse

from bottle import Bottle, run, request

app = Bottle()


@app.route('/')
def get_ip():
    client_ip = request.environ.get('REMOTE_ADDR')
    return json.dumps({"client_ip": client_ip})

@app.route('/meetup')
def mgg():
    return json.dumps({"message": "Python service response for the meetup!!!! !!"})

@app.route('/smoketest')
def smoketest():
    return json.dumps({"message": "smoke test ok"})

@app.route('/casadamoeda')
def casadamoeda():
    return json.dumps({"message": "casadamoeda test ok"})

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="HTTP API for returning a visitor's IP address.")

    parser.add_argument('hostname', default="0.0.0.0",
                        help='Host IP to listen on. ')

    parser.add_argument('port', default="8080", help='The port to listen on.')

    args = parser.parse_args()

    run(app, host=args.hostname, port=args.port)
