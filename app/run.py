from app import app
from db import db
from models import article, source
import routes
import main_feed
from threading import Thread
import time

with app.app_context():
    db.create_all()

def updating_loop():
    while True:
        with app.app_context():
            q = source.Source.query
            for src in q.all():
                try:
                    update_source(src)
                except:
                    continue
        time.sleep(15*60)

def update_source(src):
    parsed = main_feed.parsing_method(src.feed)
    articles = main_feed.articles_get(parsed)
    article.Article.insert_feed(src.id, articles)

thread = Thread(target=updating_loop)
thread.start()
app.run(debug = True)
