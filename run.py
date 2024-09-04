from flask import Flask, jsonify
import os

from actions.create_new_product import run

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.route("/get_new_product", methods=["GET"])
def get_new_product():
    try:
        print("request start 🟢")
        product = run()
        print("request finish 🔴")
        return jsonify(product)
    except Exception as e:
        return jsonify({
            "Error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
