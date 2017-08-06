# Movie class and constructor
class Movie():
    """ The Movie class creates an instance of a movie to show
    in a web page. In the webs page for each movie it will show
    the moview Title, Poster Image or other image for the movie,
    and when the user clicks on a movie the user will be presented
    with trailer for the movie for the user to watch"""
    
    # init method to create the movie object
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """ inits the class with movie_title, poster_image_url,
        trailer_youtube_url """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
