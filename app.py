from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask App"

@app.route('/about')
def about():
    return "This is simple Flask App"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
