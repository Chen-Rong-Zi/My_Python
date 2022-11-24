from flask import Flask
app = Flask(__name__)


@app.route('/')
def init():
    return 'hello chenxiangyu'



app.run()

