from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to PUCSD 13th May 2023 - 6:35 PM!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
