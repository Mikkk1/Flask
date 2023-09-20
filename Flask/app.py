from flask import Flask

# pip install redirect
# WSGI Application
app = Flask(__name__)

# Decorator:
@app.route('/') # decorator is used to register the function as a route in our app
def hello():
    return "Hello World! This is m first Flask app"

@app.route('/success/<int:score>')
def success(score):
    return "You got " + str(score)

@app.route('/success/<int:score>')
def fail(score):
    return "You failed. You got " + str(score)

@app.route('/results/<int:score>')
def result(score):
    if score > 40: 
        result =  'success'
    else
        result = 'fail'
    # return result
    return redirect(url_for(result, score= score))
if __name__ == "__main__":
    # app.run()
    app.run(debug = True)