from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info("Request received at root endpoint")
    return 'Hello, Simple Flask application'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
