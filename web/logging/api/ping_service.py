from flask import make_response
from . import api


@api.route('/ping', methods=['GET'])
def ping():
    response = make_response()
    response.status_code = 200
    return response
