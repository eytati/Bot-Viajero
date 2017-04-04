from flask import Flask
from flask.ext.pymongo import  PyMongo

app = Flask(__name__)

app.config['Direccion_BD'] = 'mongodb://<BotViajero>:<bot5917>@ds135800.mlab.com:35800/botviajero'
mongo = PyMongo(app)



a = mongo.db.Usuarios
a.insert({})
a.find({})





@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
