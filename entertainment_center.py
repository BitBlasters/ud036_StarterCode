

import media
import fresh_tomatoes

# create the movie objects
star_wars = media.Movie("Star Wars",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX",
                        "https://www.youtube.com/watch?v=vP_1T4ilm8M")

avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_wars_rogue_one = media.Movie("Rogue One: A Star Wars Story",
                                  "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                                  "https://www.youtube.com/watch?v=frdj1zb9sMY")

lord_of_the_rings = media.Movie("Lord of the Rings",
                             "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL._AC_UL320_SR214,320_.jpg",
                             "https://www.youtube.com/watch?v=rAUJN48IHXw")

avengers = media.Movie("Avengers",
                             "https://images-na.ssl-images-amazon.com/images/I/61bINjWK62L.jpg",
                             "https://www.youtube.com/watch?v=eOrNdBpGMv8")

hunger_games = media.Movie("Hunger Games",
                             "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/The-Hunger-Games-Poster1.jpg",
                             "https://www.youtube.com/watch?v=PbA63a7H0bo")

harry_potter = media.Movie("Harry Potter",
                           "https://s-media-cache-ak0.pinimg.com/originals/49/6f/58/496f5882597c4966a2ce7289d627a1a0.jpg",
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")

star_trek = media.Movie("Star Trek",
                           "http://www.impawards.com/2009/posters/star_trek_xi_ver16_xlg.jpg",
                           "https://www.youtube.com/watch?v=3PM1pvOzn_w")

matrix = media.Movie("Matrix",
                           "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                           "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# add the movie objects to a list
movies = [star_wars, avatar, star_wars_rogue_one, lord_of_the_rings, avengers, hunger_games, harry_potter, star_trek, matrix]

# send the movie list to be viewed.
fresh_tomatoes.open_movies_page(movies)
