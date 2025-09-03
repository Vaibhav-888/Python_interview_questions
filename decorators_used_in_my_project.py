from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# custom decorator for authentication and logging
def auth_and_log(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        token = request.headers.get("Authorization")

        # check for token validity
        if not token or token != "my_token":
            return jsonify({"error": "Unauthorized"}), 401
        
        # log request details
        print(f"Request to {request.path} with method {request.method}")

        return func(*args, **kwargs)
    return decorated_func

gsp_gstin_search = []

@app.route("fetch_gstin/<gstin>}", methods = ["GET"])
@auth_and_log
def fetch_gstin(gstin):
    # logic to fetch gstin from the db and return response
    data = {"data": gstin, "status": "Active"}
    gsp_gstin_search.append(data)
    return jsonify(gsp_gstin_search)

get_gstin = fetch_gstin("27AAACT2727Q1ZW")
print(get_gstin)