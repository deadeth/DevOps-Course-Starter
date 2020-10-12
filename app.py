from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

todos = [
    {'id': 1, 'title': 'First Todo', 'description': 'do this tomorrow'},
    {'id': 2, 'title': 'Second Todo', 'description': 'do this day after'},
    {'id': 3, 'title': 'Third Todo', 'description': 'do this day after that'}]


@app.route('/')
def index():
    return 'Hello World! <a href=http://127.0.0.1:5000/todo> todos</a>'


@app.route('/todo', methods=['GET'])
@app.route('/todo/', methods=['GET'])
def todolist():
    return render_template('index.html', todos=todos)


@app.route('/todo/{todoId}', methods=['GET'])
@app.route('/todo/{todoId}/', methods=['GET'])
def todolist():
    return render_template('index.html', todos=todos)


@app.route('/todo/reset', methods=['GET'])
def todoreset():
    todos.append({})
    todos.clear()
    return 'success'


@app.route('/todo', methods=['POST'])
def addtotodolist():
    todos.append({'id': 4, 'title': request.form['title'], 'description': request.form['description']})
    return render_template('index.html', todos=todos)


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS)


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = {'id': id, 'title': title, 'status': 'Not Started'}

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


if __name__ == '__main__':
    app.run()
