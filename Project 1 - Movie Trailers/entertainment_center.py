import fresh_tomatoes
import media


def run():
    """
    The method that creates the movie list and run the given script
    """
    zootopia = media.Movie("Zootopia",
                     "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                     "https://lumiere-a.akamaihd.net/v1/images/movie_poster_zootopia_866a1bf2.jpeg?region=0%2C0%2C300%2C450")  # noqa

    suicide = media.Movie("Suicide Squad",
                    "https://www.youtube.com/watch?v=CmRih_VtVAs",
                    "http://cdn.collider.com/wp-content/uploads/2016/06/suicide-squad-poster-400x600.jpg")  # noqa

    jurassic = media.Movie("Jurassic Park 1",
                     "https://www.youtube.com/watch?v=lc0UehYemQA",
                     "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg")  # noqa

    move_list = [zootopia, suicide, jurassic]
    fresh_tomatoes.open_movies_page(move_list)

run()
