import requests



url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
    285
)
data = requests.get(url)
data = data.json()
poster_path = data['poster_path']

print(poster_path)