from flask import Flask
import socket   

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

PORT = 8000
MESSAGE = '''<body>
             <h1 style="color:blue;">Hello, world! from {} @ IP {} </h1>
             <h2 style="color:green;"> Python code tends to be simpler </h2>
             </body>
             <style>
             body {
             background-image: url('CariBeach.jpg');
             }
             </style>'''.format(hostname,IPAddr)

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
