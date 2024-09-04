from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

from actions.create_new_product import run

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

# Initialize the Limiter
limiter = Limiter(
    get_remote_address,  # Use the remote IP address of the request as the key for rate limiting
    app=app,
    default_limits=["100 per hour"]  # Default limit if no other specific limit is defined
)


@app.route("/get_new_product", methods=["GET"])
@limiter.limit("5 per minute")  # Limit this specific route to 10 requests per minute
def get_new_product():
    try:
        product = run()
        return jsonify(product)
    except Exception as e:
        return jsonify({
            "Error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
