from flask import request
from flask_restful import Resource
from models import db, News

class NewsResource(Resource):
    def get(self, news_id=None):
        if news_id:
            news = News.query.get(news_id)
            if not news:
                return {'message': 'News not found'}, 404
            return {
                'id': news.id,
                'title': news.title,
                'content': news.content,
                'user_id': news.user_id
            }
        news_list = News.query.all()
        return [{'id': n.id, 'title': n.title, 'content': n.content, 'user_id': n.user_id} for n in news_list]

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

    def put(self, news_id):
        data = request.get_json()
        news = News.query.get(news_id)
        if not news:
            return {'message': 'News not found'}, 404
        news.title = data['title']
        news.content = data['content']
        db.session.commit()
        return {'message': 'News updated successfully'}, 200

    def delete(self, news_id):
        news = News.query.get(news_id)
        if not news:
            return {'message': 'News not found'}, 404
        db.session.delete(news)
        db.session.commit()
        return {'message': 'News deleted successfully'}, 200
