from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news ,process_news



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    usa_news = get_news('us')
    australia_news = get_news('au')
    sa_news = get_news('za')

    title = 'news website'

    return render_template('index.html', title = title, us = usa_news, australia = australia_news, sa =sa_news )
