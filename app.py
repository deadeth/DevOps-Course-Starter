import requests
from flask_config import Config
from flask import Flask, render_template, request, redirect, url_for, jsonify
import session_items as session

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! <a href=http://127.0.0.1:5000/todo> todos</a>'


@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todolist():
    return render_template('index.html', todos=None)


@app.route('/todo/{todoId}', methods=['GET'])
@app.route('/todo/{todoId}/', methods=['GET'])
def gettodoitem():
    return render_template('index.html', todos=None)


@app.route('/todo/reset', methods=['GET'])
def resettodos():
    return 'success'


@app.route('/trello', methods=['GET'])
def gettrelloinfo():
    payload = {'member': Config.MEMBER_ID,
               'key': Config.TRELLO_API_KEY,
               'token': Config.TRELLO_TOKEN}
    r = requests.get('https://api.trello.com/1/members/me', params=payload)
    return jsonify(r.json())


@app.route('/trello/boards', methods=['GET'])
def getboards():
    payload = {'fields': ['name', 'url'],
               'key': Config.TRELLO_API_KEY,
               'token': Config.TRELLO_TOKEN}
    r = requests.get('https://api.trello.com/1/members/me/boards', params=payload)
    return jsonify(r.json())


@app.route('/trello/boards/<string:boardid>/lists', methods=['GET'])
def getlistsofboard(boardid):
    payload = {'fields': ['name', 'url'],
               'key': Config.TRELLO_API_KEY,
               'token': Config.TRELLO_TOKEN}
    r = requests.get(f'https://api.trello.com/1/boards/{boardid}/lists', params=payload)
    return jsonify(r.json())


@app.route('/trello/list/<string:listid>', methods=['GET'])
def getcardsoflist(listid):
    payload = {'fields': ['name', 'url', 'closed', 'pos'],
               'key': Config.TRELLO_API_KEY,
               'token': Config.TRELLO_TOKEN}
    r = requests.get(f'https://api.trello.com/1/lists/{listid}/cards', params=payload)
    return jsonify(r.json())


@app.route('/todo', methods=['POST'])
def addtotodolist(name):
    r = requests.post('https://api.trello.com/1/cards',
                      data={'key': Config.TRELLO_API_KEY,
                            'token': Config.TRELLO_TOKEN,
                            'name': name,
                            'idList': getboards[0]['id']
                            })
    rj = r.json()
    return render_template('index.html', todos=None)


if __name__ == '__main__':
    app.run()
