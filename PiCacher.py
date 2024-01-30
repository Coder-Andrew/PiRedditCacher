from MongoService import IMongoService, MongoService
from filehandler import JsonFileStore
from RedditService import RedditService
from datetime import datetime

class PiCacher:
    def __init__(self, mongoService: IMongoService, jsonFileStore: JsonFileStore, redditService: RedditService):
        self.mongoService = mongoService
        self.jsonFileStore = jsonFileStore
        self.redditService = redditService

    def cache_posts(self, timeframe = 'week', url = "https://www.reddit.com/r/Python/top/.json?t="):
        # Combine cached posts with new posts
        posts = self.redditService.get_reddit_posts(time = timeframe, url=url)

        if self.mongoService.test_connection():
            stored_posts = self.jsonFileStore.read()

            print(f'Successful connection to {self.mongoService.name} sent {len(posts)} posts + {len(stored_posts)} cached posts at: {datetime.now()}')
            
            posts += stored_posts                   # Get posts from json cache
            self.mongoService.create_many(posts)    # Save posts to db
            self.jsonFileStore.return_clear()       # Clear cache
        
        else:
            print(f'---Unsuccessful connection to {self.mongoService.name} at: {datetime.now()}\n\tCaching: {len(posts)}, cached: {len(self.jsonFileStore)}')
            
            self.jsonFileStore.write(posts)         # Add posts to cache


if __name__ == '__main__':
    mongoService = MongoService("localhost", 27017, "testdb","RedditPosts")
    jsonFileStore = JsonFileStore('cache.json')
    redditService = RedditService()

    pc = PiCacher(mongoService, jsonFileStore, redditService)
    pc.cache_posts('week')