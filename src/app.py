  
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/tasks', methods=['Post'])
def create_task():
    print(request.json)
    return 'received'


if __name__ == "__main__":
    app.run(debug=True)