import os
from flask import Flask

app = Flask(__name__)

@app.route("/db")
def hello():
    return "Hello World from alperenokur.com/db"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Cloud Run's expected port
    app.run(host="0.0.0.0", port=port)
