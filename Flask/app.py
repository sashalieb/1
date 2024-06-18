from flask import Flask, render_template
from flask_migrate import Migrate
from models import db
from config import Config
from resources.user import UserResource
from resources.news import NewsResource
from flask_restful import Api
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')
api.add_resource(NewsResource, '/api/news', '/api/news/<int:news_id>')

@app.route('/')
def home():
    return render_template('users.html', title="Users")

@app.route('/users')
def show_users():
    return render_template('users.html', title="Users")

@app.route('/news')
def show_news():
    return render_template('news.html', title="News")

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect, url_for

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.form
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('show_users'))

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('show_users'))

@app.route('/api/news', methods=['POST'])
def add_news():
    data = request.form
    new_news = News(
        title=data['title'],
        content=data['content'],
        user_id=data['user_id']
    )
    db.session.add(new_news)
    db.session.commit()
    return redirect(url_for('show_news'))

@app.route('/api/news/<int:news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('show_news'))

class UserResource(Resource):
    def get(self, user_id=None):
        # Оставляем текущий код
        pass

    def post(self):
        data = request.get_json()
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

    # Оставляем текущий код


class NewsResource(Resource):
    # Оставляем текущий код

    def post(self):
        data = request.get_json()
        new_news = News(
            title=data['title'],
            content=data['content'],
            user_id=data['user_id']
        )
        db.session.add(new_news)
        db.session.commit()
        return {'message': 'News created successfully'}, 201

    # Оставляем текущий код
