import access
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return access.decode(access.key, access.coinbase_id)

if __name__ == "__main__":
    application.run()
