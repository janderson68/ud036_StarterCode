""" The goal of the entertainment_center.py is to
instantiate instances of the movie class and display them on a HTML webpage """
import media
import fresh_tomatoes
# Jude Anderson
# 10/13/18
# A python file which creates several instances of the Movie object,
# stores them in array, and displays them on an html page
IRON_BLOODED_ORPHANS = media.Movie("Gundam: Iron Blooded Orphans",
                                   "A story about orphans on mars caught up"
                                   +"in a war and trying to own their own lives.",
                                   "IRON_BLOODED.jpg",
                                   "https://www.youtube.com/watch?v=IddxplDVGw8")

BOKU_NO_HERO_ACADEMIA = media.Movie("Boko no Hero Academia",
                                    "A story about a quirkless kid who becomes"+
                                    " the greatest super hero of all",
                                    "BOKU_NO_HERO.jpg",
                                    "https://www.youtube.com/watch?v=wIb3nnOeves")

DARLING_IN_THE_FRANXX = media.Movie("Darling in a FRANXX",
                                    "A very good anime which did not resolve anything, "+
                                    " but relys on the power of friendship",
                                    "FRANXX.jpg",
                                    "https://en.wikipedia.org/wiki/Darling_in_the_Franxx")

ONE_PIECE = media.Movie("One Piece",
                        "A tale of a young boy who will become the king of the pirates",
                        "ONE_PIECE.jpg",
                        "https://en.wikipedia.org/wiki/One_Piece")

MOVIES = [IRON_BLOODED_ORPHANS, BOKU_NO_HERO_ACADEMIA, DARLING_IN_THE_FRANXX, ONE_PIECE]
fresh_tomatoes.open_movies_page(MOVIES)
