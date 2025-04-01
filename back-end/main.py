from flask import Flask, send_from_directory
import os

app = Flask(__name__)
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../front-end")

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, "index.html")
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)

    