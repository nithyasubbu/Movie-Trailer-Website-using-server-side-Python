# Movie-Trailer-Website-using-server-side-Python
Designed and developed a server-side python code to create a "Movie Trailer Website" 


Movie Trailer Website:

The idea of this project is to write a server-side python code to implement a static web page comprising of movie trailers. User can visit the web page and choose any movie he/she likes and can directly see their youtube trailers. 
Implementation: User when logged in, can see the different movie poster images with their titles, storylines, imdb ratings and genres. The visual appeal of the background is kept simple and sober. Theme chosen: black. Four different background images are chosen and two are kept static and two are kept scrolling for the scrolling effect in the background.

Under the hood details:

There are five files namely:
a. media.py - A simple python class "Movie" containing all the movie attributes and movie methods
Movie attributes : movie title, movie storyline, movie poster image, movie youtube trailer url, movie imdb rating and movie genre
Movie methods: show Trailer() to display the movie trailer for every movie instance

b. entertainment.py - Main() function lets movie instance creation using media.Movie() (after importing movie). 12 movie instances were created for the scope of the project. And the movie instances are passed as list objects to movie_list. On calling fresh_tomatoes.open_movies_page(movie_list), the list of movie objects are then passed as input and converted to an output html page for viewing movie website trailers

c. fresh_tomatoes.py - This python file basically serves as a template to convert a list of movie insatnces into html page. Changes to suit the requirements of a simple, user-friendly, visually appealing movie trailer website is made in this python file 

User details:

Run intructions:

To execute the following implementation, the user is supposed to download the zip file movie_Trailer_FinalProject. The user then and save the zip file in a convenient place and note its location. 

Windows: To run, please go to the location of the unzipped folder (in C drive or any other drive) where the python file entertainment.py resides and then run>> "C:\...\..python" entertainment_center.py 

OS: To run, open the terminal and go to the location where the unzipped folder is present. Go inside the folder (where entertainment.py file is present), then run>> python entertainment_center.py


This directly takes the user to the html page that can be opened on any browser and the user can then view their favorite movie trailers
   
