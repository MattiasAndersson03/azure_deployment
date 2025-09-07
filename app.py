from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<center><h1>Welcome to the Flask App! Azure</h1></center>"

if __name__ == "__main__":
    app.run()

