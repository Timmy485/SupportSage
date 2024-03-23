from os import environ
from app import create_app, database


DEBUG = environ.get("DEBUG")
HOST = environ.get("HOST")
PORT = environ.get("PORT")

application = create_app()

if __name__ == "__main__":
    application.run(host=HOST, port=PORT, debug=DEBUG, threaded=True)
