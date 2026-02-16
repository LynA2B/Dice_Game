from flask import Flask

app = Flask(__name__)

# App metadata
APP_NAME = "My Flask App"
APP_VERSION = "1.0"
APP_DESCRIPTION = "A basic Flask application"

@app.route("/")
def home():
    return render_template(dice.html)

if __name__ == "__main__":
    app.run(debug=True)