from __main__ import app
from flask import make_response,jsonify


@app.route('/status', methods=['GET'])
def test_route():
    return make_response(jsonify({"APPLICATION RUNNING": "Flask Back-End Application is running correctly"}, 200))