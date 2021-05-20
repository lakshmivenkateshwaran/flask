#from flask import Flask
#from flask_restful import Resource, Api

#app = Flask(__name__)
#api = Api(app)

#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

#api.add_resource(HelloWorld, '/')

#if __name__ == '__main__':
#    app.run(debug=True)

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/hi')
def hi_world():
    return "Hii Guys!!"

@app.route('/user/<username>')
def user(username):
    return "Welcome user: %s" %escape(username)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)

