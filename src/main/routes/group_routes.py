from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.group.group_list import group_list_composer

group_route_bp = Blueprint("group_routes", __name__)

@group_route_bp.route("/group/list", methods=["POST"])
def login_user():
    http_response = request_adapter(request, group_list_composer())
    return jsonify(http_response.body), http_response.status_code

