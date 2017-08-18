# Importing the module webbrowser
import webbrowser


class Movie():

    # Creating Movie contructor to initialize the movie instance attributes
    # such as movie_title, movie_storyLine, movie_poster_image_url,
    # movie_trailer_url, movie_imdb_rating, movie_genre
    def __init__(
            self,
            movie_title,
            movie_storyLine,
            movie_poster_image_url,
            movie_trailer_url,
            movie_imdb_rating,
            movie_genre):

        # VALID_RATINGS = ['PG-13','G','R','GR']

        # Using self keyword to initialize the movie attributes to each movie
        # instance
        self.movie_title = movie_title
        self.movie_storyLine = movie_storyLine
        self.movie_poster_image_url = movie_poster_image_url
        self.movie_trailer_url = movie_trailer_url
        self.movie_imdb_rating = movie_imdb_rating
        self.movie_genre = movie_genre

    # Method to show the movie trailers
    def show_Trailer(self):

        # Using open method from webbrowser module, any video urls (from web)
        # can be directly displayed
        webbrowser.open(self.movie_trailer_url)
