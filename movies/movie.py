import webbrowser
import video
#from video import Video

class Movie(video.Video):
    """This plays stuff"""
    def __init__(self, movie_attrib):
        self.storyline = movie_attrib['storyline']
        self.poster_image_url = movie_attrib['poster_image_url']
        self.trailer_youtube_url = movie_attrib['trailer_youtube_url']
        #video.Video(self, movie_attrib['title'], movie_attrib['duration'])
        video.Video.__init__(self, movie_attrib['title'], movie_attrib['duration'])

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
