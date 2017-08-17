import webbrowser
import os
import re

# Styles and scripting for the page
#Basically, some html/css styling is done to make the movie trailer webpage look more appealing

#Title is indicated as "Nithya's Movie Trailer Website!"

#body: background-color: black (for the night effect), background-images: 4 images are linked as urls, background-attachment: Two are static and two are scrolling for the visual appeal
#body: background-repeat: no two images are repeated more than once for the better visual effect
#body: background-position: all the images are alighned center of the screen

#body: body color is defined as white as the text is emphasized against black background

#movie-tile: background-color is set to background-color: #fdeef4(light pink background).And the text color in the movie-tile: black (for the background contrast as the text is emphasized)
#scale-media frame's background color is set to black by default

#trailer video height and width are set to 120% each for better visibility

main_page_head = '''
<head>
    <meta charset="utf-8">
    <meta name="theme-color" content="#29F018">
    <title>Fresh Tomatoes!</title>
    <title>Nithya's Movie Trailer Website!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 100px;
        }
        body{
            background-color: black;
            background-image: url("https://i.pinimg.com/564x/b9/bf/6b/b9bf6b99470fe5ed5b35857a816af55e.jpg"),url("http://youtellconcerts.com/wp-content/uploads/2012/10/hollywood-sign1999_fnokt4ke2.jpg"),url("http://themeparkadventure.com/wp-content/uploads/2015/12/WWoHP-castle-grand-opening-date-in-sky-4-7-16.jpg"),url("http://leelanau.org/wp-content/uploads/lights_camera_action.jpg");
            background-attachment: scroll,fixed,fixed,scroll;
            background-repeat: no-repeat, no-repeat, no-repeat, repeat;
            background-position: center, center, center, center;
            
        }
        body{
            color: white;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 540px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 120%;
            height: 120%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #fdeef4;
            color: black;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar

#Under main page contents, "Nithya's Movie Trailer Website >> Choose your favorite movie to get a glimpse of what's in store!!" for the user to see who created it

main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Nithya's Movie Trailer Website >></a>
            <a class="navbar-brand" href="#">Choose your favorite movie to get a glimpse of what's in store!!</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template

#movie_tile_content: A single movie instance template is created in such as way that the user gets to see all the information about the movie such as movie title, story line, imdb rating, genre

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{movie_poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <h4>{movie_storyLine}</h4>
    <h5>{movie_genre}</h5>
    <h6>{movie_imdb_rating}</h6>
</div>
'''

#This method precisely extracts the movie contents and matches youtube trailers by their group ID and assigns it to each movie instance
#Content appends each movie instance attribute information and returns the same to open_movies_page() method
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.movie_trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.movie_trailer_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.movie_title,
            movie_storyLine = movie.movie_storyLine,
            movie_poster_image_url=movie.movie_poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_imdb_rating= movie.movie_imdb_rating,
            movie_genre = movie.movie_genre
        )
    return content

#Method open_movie_page() takes the movie list as an argument and creates a fresh_tomatoes.html file in the write mode
#It then creates the main page content with the method to create_movie_tiles_content(taking movies list as an argument)
#This function in turn matches youtube trailers by their group IDs and adds the movie attribute information to the contents
#This rendered content + main page chead is then written to the html page for the user to view the movie trailers (with all their info: story, imdb rating, title, genre)
#It then opens the absolute path of the html file created using the webbrowser module.
def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible