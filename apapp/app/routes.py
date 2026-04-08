from flask import request, jsonify

def register_routes(app):

    @app.route("/")
    def home():
        return "Shallow API is running."

    @app.route("/chat", methods=["POST"])
    def chat():
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "")

        return jsonify({
            "reply": f"Shallow received: {user_message}"
        })
