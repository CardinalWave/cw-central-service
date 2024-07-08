#pylint: disable=line-too-long
from flask import Flask
from src.main.routes.user_routes import user_route_bp
from src.main.routes.group_routes import group_route_bp
from src.main.routes.chat_routes import chat_route_bp
from src.data.erros.handlers import handle_bad_request, handle_not_found, handle_internal_server_error
from src.data.erros.domain_errors import BadRequestError, NotFoundError, InternalServerError

app = Flask(__name__)

# Registrar manipuladores de erro
app.register_error_handler(BadRequestError, handle_bad_request)
app.register_error_handler(NotFoundError, handle_not_found)
app.register_error_handler(InternalServerError, handle_internal_server_error)

# Register Blueprints
app.register_blueprint(user_route_bp)
app.register_blueprint(group_route_bp)
app.register_blueprint(chat_route_bp)
