from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news ,process_news


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


# Views

# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     usa_news = get_news('us')
#     australia_news = get_news('au')
#     sa_news = get_news('za')

#     title = 'news website'
#     message = 'wanjema'

#     return render_template('index.html', title = title ,message = message )
