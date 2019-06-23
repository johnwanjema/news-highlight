from flask import render_template
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
   
    title = "News highlight"
    return render_template('index.html',title =title, sources = news_sources)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_articles(id)
    title = f"{id}"
    

    return render_template('articles.html', article = article, name=id)