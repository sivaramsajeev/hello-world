from flask import Flask

PORT = 8000
MESSAGE = '''<h1>Hello, world! from Python Flask</h1>
             <h2> Python code tends to be simpler </h2>'''

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
