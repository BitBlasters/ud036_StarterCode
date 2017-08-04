# Movie class and constructor
class Movie():
    """ The Movie class creates an instance of a moview object to show
    in a web page"""
    # init method to create the movie object
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """ inits the class with movie_title, poster_image_url,
        trailer_youtube_url """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
