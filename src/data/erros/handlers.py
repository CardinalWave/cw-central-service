from flask import jsonify


def handle_bad_request(error):
    response = jsonify({"error": error.message})
    response.status_code = 400
    return response


def handle_not_found(error):
    response = jsonify({"error": error.message})
    response.status_code = 404
    return response


def handle_internal_server_error(error):
    response = jsonify({"error": error.message})
    response.status_code = 500
    return response
