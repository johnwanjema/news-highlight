class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,author,):
        self.id =id
        self.name = name
        self.author =author
        self.title = title

class Articles:
    '''
    News articles to define article Objects
    '''
    def __init__(self,name,title,description,url,urlToImage,publishesAt,content):
        self.name = name
        self.title = title  
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishesAt
        self.content = content
        



