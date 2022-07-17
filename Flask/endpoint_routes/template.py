from __main__ import app
from flask import make_response, jsonify

@app.route('/template', methods=['GET'])
def template_route():
    return make_response(jsonify({"Hello" : "Hello"}), 200)