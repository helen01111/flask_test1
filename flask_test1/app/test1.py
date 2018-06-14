'''
Created on 2018/06/11

@author: w-sun
'''

from flask import Flask


app=Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello,World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

@app.route('/sum/<int:id1>/<int:id2>')
def sumab(id1,id2):
    c=id1+id2
    return '%s ' % c

if __name__ == '__main__':
    app.run(debug=True)