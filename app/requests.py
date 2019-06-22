import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=03d3f69ba4844b8e94dc1582f0dc69b9'


def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None           
            
        # news_results_list = get_news_response['results']
        news_results = process_news(news_results)


    return news_results

def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain movie details
    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        news_object = News(id,name)
        news_results.append(news_object)

    return news_results