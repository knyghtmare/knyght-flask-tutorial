from flask import (
                Flask,
                render_template,
                url_for, request,
                redirect)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    todo_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.todo_id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    delete_this_task = Todo.query.get_or_404(todo_id)

    try:
        db.session.delete(delete_this_task)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue deleting the task"


@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    task = Todo.query.get_or_404(todo_id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)
