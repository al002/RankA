import pymongo
import requests

mongo_uri = 'localhost:27017'
mongo_db = 'torrents'
mongo_collection = 'movieId'

client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]

movie_url = """http://movie.douban.com/j/search_subjects?
    type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=100&page_start=0"""

r = requests.get(movie_url)
movies = r.json()['subjects']

for movie in movies:
    found = db['movieId'].find({'movie_id': movie['id']}).count()

    if not found:
        db['movieId'].insert({'movie_id': movie['id']})
        print(movie['id'])
