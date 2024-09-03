from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome"



if __name__ == "__main__":
    app.run(debug=True)
