from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.groups.group_list_composer import group_list_composer
from src.main.composers.groups.group_join_composer import group_join_composer
from src.main.composers.groups.group_create_composer import group_create_composer
from src.main.composers.groups.group_leave import group_leave_composer

group_route_bp = Blueprint("group_routes", __name__)


@group_route_bp.route("/group/list", methods=["POST"])
def group_list():
    http_response = request_adapter(request, group_list_composer())
    return jsonify(http_response.body), http_response.status_code


@group_route_bp.route("/group/join", methods=["POST"])
def group_join():
    http_response = request_adapter(request, group_join_composer())
    return jsonify(http_response.body), http_response.status_code


@group_route_bp.route("/group/leave", methods=["POST"])
def group_leave():
    http_response = request_adapter(request, group_leave_composer())
    return jsonify(http_response.body), http_response.status_code


@group_route_bp.route("/group/create", methods=["POST"])
def group_create():
    http_response = request_adapter(request, group_create_composer())
    return jsonify(http_response.body), http_response.status_code
