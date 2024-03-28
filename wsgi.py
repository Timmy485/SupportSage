from os import environ
from app import create_app, database


DEBUG = environ.get("DEBUG", "True")
HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", 5050))

application = create_app()

if __name__ == "__main__":
    application.run(host=HOST, port=PORT, debug=DEBUG, threaded=True)
