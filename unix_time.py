import time
import os
from flask import Flask

app = Flask(__name__)

@app.route("/unix_time/")
def get_time():
    return str(time.time())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "6738"))
    app.run(host="", port=port)
