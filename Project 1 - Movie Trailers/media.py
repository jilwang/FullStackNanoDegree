class Movie:
    def __init__(self, title='', trailer_youtube_url='', poster_image_url=''):
        """
        This class represents a Movie in the navigation page,
        which contains the title and poster to display,
        and a link to the trailer on youtube
        """
        
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
