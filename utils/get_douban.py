import time
import pymongo
import requests


mongo_uri = 'localhost:27017'
mongo_db = 'torrents'
mongo_collection = 'movieId'
douban_api = 'http://api.douban.com/v2/movie/subject/'

client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]

movies = db.movieId.find()

for movie in movies:
    id = movie['movie_id']
    print(movie['movie_id'])
    found = db['movies'].find({"id": movie['movie_id']}).count()
    
    if not found:
        try:
            r = requests.get(douban_api + movie['movie_id'])
            print(r)
            db['movies'].insert(r.json())
            time.sleep(3)

            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print "And you get an HTTPError:", e.message
        except requests.exceptions.ConnectionError as e:
            db['failed_id'].insert({'id': movie['movie_id']})
            print('request failed')


