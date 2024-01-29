from MongoService import IMongoService, MongoService
from filehandler import JsonFileStore
from RedditService import RedditService

from RedditModel import RedditModel

class PiCacher:
    def __init__(self, mongoService: IMongoService, jsonFileStore: JsonFileStore, redditService: RedditService):
        self.mongoService = mongoService
        self.jsonFileStore = jsonFileStore
        self.redditService = redditService

    def cache_posts(self, timeframe = 'week', url = "https://www.reddit.com/r/Python/top/.json?t="):
        # Combine cached posts with new posts
        posts = self.redditService.get_reddit_posts(time = timeframe, url=url) + self.jsonFileStore.read()

        if self.mongoService.test_connection():
            self.mongoService.create_many(posts)
            self.jsonFileStore.return_clear()
        else:
            self.jsonFileStore.write(posts)


if __name__ == '__main__':
    mongoService = MongoService("localhost", 27017, "testdb","RedditPosts")
    jsonFileStore = JsonFileStore('cache.json')
    redditService = RedditService()

    pc = PiCacher(mongoService, jsonFileStore, redditService)
    pc.cache_posts('week')