import webbrowser

class Movie():
    """This plays stuff"""
    def __init__(self, movie_attrib):
        self.title = movie_attrib['title']
        self.storyline = movie_attrib['storyline']
        self.poster_image_url = movie_attrib['poster_image_url']
        self.trailer_youtube_url = movie_attrib['trailer_youtube_url']

    def show_trailer(self):
        webbrowser.open(self.trailer)
