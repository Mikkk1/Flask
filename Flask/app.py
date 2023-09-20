from flask import Flask
# WSGI Application
app = Flask(__name__)

# Decorator:
@app.route('/') # decorator is used to register the function as a route in our app
def hello():
    return "Hello World! This is m first Flask app"

if __name__ == "__main__":
    app.run()
    # app.run(debug = True)