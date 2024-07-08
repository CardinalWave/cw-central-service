from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.chat.chat_join_composer import chat_join_composer

chat_route_bp = Blueprint("chat_routes", __name__)


@chat_route_bp.route("/chat/join", methods=["POST"])
def chat_join():
    http_response = request_adapter(request, chat_join_composer())
    return jsonify(http_response.body), http_response.status_code
