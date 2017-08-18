import time

# Import media.py to create class instances of class Movie()
import media

# Import fresh_tomatoes.py to call the open_movies_page() method passing
# the movie list
import fresh_tomatoes

# Implementing the movie class instance creation in main function


def main():

    # Creating 12 different movie instances using media.Movie() >> __init__
    # method
    slumdogMillionaire = media.Movie(
        "Slumdog Millionaire",
        "A boy from the slums fights all odds and wins the life race",
        "https://upload.wikimedia.org/wikipedia/en/9/92/Slumdog_Millionaire_poster.png",  # noqa
        "https://www.youtube.com/watch?v=AIzbwV7on6Q",
        "IMDB : 8.0/10",
        "Genre: Drama")

    lion = media.Movie(
        "Lion",
        "A boy goes in search of his family with his destiny rewritten",
        "https://s-media-cache-ak0.pinimg.com/originals/73/ae/02/73ae020933b4858dc3a8b72de977899f.jpg",  # noqa
        "https://www.youtube.com/watch?v=-RNI9o06vqo",
        "IMDB : 8.1/10",
        "Genre: Bio/Drama")

    spidermanHomecoming = media.Movie(
        "Spiderman Homecoming",
        "An ordinary boy with an extra-ordinary will to do common good - web",
        "https://cdn.vox-cdn.com/uploads/chorus_asset/file/8571065/spider_man_poster2.jpg",  # noqa
        "https://www.youtube.com/watch?v=U0D3AOldjMU",
        "IMDB : 7.9/10",
        "Genre: Sci-fi/Adventure")

    wonderWoman = media.Movie(
        "Wonder Woman",
        "A woman who is truly a wonder",
        "https://pbs.twimg.com/media/DAC5qDlVYAAVd5v.jpg",
        "https://www.youtube.com/watch?v=VSB4wGIdDwo",
        "IMDB : 7.9/10",
        "Genre: Sci-fi/Adventure")

    suicideSquad = media.Movie(
        "Suicide Squad",
        "Supremely powerful evil people(squad) fighting the nation's enemy ",
        "https://i.ytimg.com/vi/CmRih_VtVAs/maxresdefault.jpg",
        "https://www.youtube.com/watch?v=CmRih_VtVAs",
        "IMDB : 6.2/10",
        "Genre: Fantasy/Adventure")

    avengers = media.Movie(
        "Avengers",
        "Super powers: good, bad and ugly culminate for a common good",
        "https://orig00.deviantart.net/d0f1/f/2016/007/0/0/avengers_3_infinity_war_poster_by_mrvideo_vidman-d9n5252.png",  # noqa
        "https://www.youtube.com/watch?v=Jtm8WLHoGcQ",
        "IMDB : 8.1/10",
        "Genre: Sci-fi/Action")

    theDarkKnight = media.Movie(
        "The Dark Knight",
        "It's not who I am underneath, but what I do that matters",
        "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY",
        "IMDB : 9.0/10",
        "Genre: Action/Adventure")

    midnightInParis = media.Movie(
        "Midnight in Paris",
        "Vacationing in Paris with his fiance brings an unexpected turn",
        "https://images-na.ssl-images-amazon.com/images/I/61FbcrpxSTL._SX342_.jpg",  # noqa
        "https://www.youtube.com/watch?v=FAfR8omt-CY",
        "IMDB : 7.7/10",
        "Genre: Comedy/Fantasy")

    sleeplessInSeattle = media.Movie(
        "Sleepless In Seattle",
        "Death of his wife takes him to Seattle for a life full of surprises",
        "http://www.gstatic.com/tv/thumb/movieposters/14843/p14843_p_v8_aa.jpg",  # noqa
        "https://www.youtube.com/watch?v=4J7gg1V0oak",
        "IMDB : 6.8/10",
        "Genre: Comedy/Drama")

    hobbit = media.Movie(
        "Hobbit",
        "The weird creature",
        "https://static2.hypable.com/wp-content/uploads/2012/09/New-Hobbit-Poster.jpg",  # noqa
        "www.youtube.com/watch?v=4QZ4tdIPGJQ",
        "IMDB : 7.9/10",
        "Genre: Adventure/Fantasy")

    thePrestige = media.Movie(
        "The Prestige",
        "An illusion gone horribly wrong for two magicians of 19th century",
        "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
        "https://www.youtube.com/watch?v=o4gHCmTQDVI",
        "IMDB : 8.5/10",
        "Genre: Sci-fi/Mystery")

    TheImitationGame = media.Movie(
        "The Imitation Game",
        "Genius Alan Turing,trying to crack the enigmacode during world war 2",
        "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",  # noqa
        "https://www.youtube.com/watch?v=S5CjKEFb-sM",
        "IMDB : 8.1/10",
        "Genre: Bio/Drama/Thriller")

    # Passing the movie instances as list objects to a movie_List
    movie_List = [
        slumdogMillionaire,
        lion,
        spidermanHomecoming,
        wonderWoman,
        suicideSquad,
        avengers,
        theDarkKnight,
        midnightInParis,
        sleeplessInSeattle,
        hobbit,
        thePrestige,
        TheImitationGame]

    # Passing the movie_List as an input to open_movies_page() method (from
    # fresh_tomatoes.py) to generate a html page containing the aforementioned
    # movie urls
    fresh_tomatoes.open_movies_page(movie_List)

    # To list the media movie's documentation details & Valid ratings
    # print(media.Movie.__doc__)
    # print(media.Movie.VALID_RATINGS)


# Calling main method
if __name__ == '__main__':
    main()
