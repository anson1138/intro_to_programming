import movie

toy_story = movie.Movie({
    'title':'Toy Story',
    'storyline':'A boy and his toys that come to life.',
    'poster_image_url':'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450',
    'trailer_youtube_url':'https://www.youtube.com/watch?v=SgoiKLFBA3Q',
    'duration':'1hr30min'
})

print(toy_story.storyline)

avatar = movie.Movie({
    'title':'Avatar',
    'storyline':'A guy on an alient planet',
    'poster_image_url':'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',
    'trailer_youtube_url':'https://www.youtube.com/watch?v=cRdxXPV9GNQ',
    'duration':'2hr20min'
})

wild_kratt = movie.Movie({
    'title':'Wild Kratt HI Branden!!!',
    'storyline':'Two brothers who really love animals',
    'poster_image_url':'https://s-media-cache-ak0.pinimg.com/originals/9f/d8/b1/9fd8b10b9f1db875417d8ee3817b9643.jpg',
    'trailer_youtube_url':'https://www.youtube.com/watch?v=y9DxVImA0lk',
    'duration':'30min'
})

print(avatar.title)
print(avatar.storyline)
print(avatar.duration)

#avatar.show_trailer()

#movies = [toy_story, avatar, wild_kratt]
#fresh_tomatoes.open_movies_page(movies)

