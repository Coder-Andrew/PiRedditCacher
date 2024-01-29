from pymongo import MongoClient
from json import dumps
from abc import ABC, abstractmethod
from typing import List, Dict

from RedditModel import RedditModel

class IMongoService(ABC):
    # This is a lot of unused methods...
    @abstractmethod
    def test_connection(self):
        pass

    @abstractmethod
    def create(self, newModel: RedditModel):
        pass

    @abstractmethod
    def create_many(self, newModels: List[RedditModel]):
        pass

    @abstractmethod
    def update(self, model: RedditModel):
        pass

    @abstractmethod
    def create_update(self, model: RedditModel):
        pass

    @abstractmethod
    def create_update_many(self, model: RedditModel):
        pass

    @abstractmethod
    def exists(self, model: RedditModel):
        pass

    @abstractmethod
    def get_all(self) -> List[RedditModel]:
        pass


# I don't think this adheres to SOLID correctly... maybe I should pass in the mongoclient as a dependency
# via constructor injection...
class MongoService(IMongoService):
    def __init__(self, ip: str, port: int, dbname: str, collectionName: str, name: str = "DefaultConnection"):
        try:
            self.name = name
            self.client = MongoClient(ip, port, serverSelectionTimeoutMS=5000)
            self.db = self.client[dbname]

            self.collection = self.db[collectionName]

        except Exception as e:
            raise ValueError(f"Error while connecting to Mongo: {e}")


    def exists(self, model: RedditModel) -> bool:
        if self.collection.find_one({'url' : model.url}):
            return True
        return False


    def create(self, newModel: RedditModel) -> int:
        try:
            return self.collection.insert_one(newModel.__dict__).inserted_id
        
        except Exception as e:
            raise ValueError(f'Error while inserting: {newModel.__dict__}\n\t{e}')
        

    def test_connection(self):
        try:
            self.client.server_info()
            return True
        except:
            return False


    def update(self, model: RedditModel):
        try:
            self.collection.update_one({'url' : model.url}, {'$set' : model.__dict__})
            return True
        except Exception as e:
            raise ValueError(f'Error finding model {model.__dict__} --- {e}')
        

    def create_update(self, model: List[RedditModel]):
        if self.exists(model):
            return self.update(model)
        else:
            return self.create(model)


    def create_update_many(self, modelList: List[RedditModel]):
        for model in modelList:
            self.create_update(model)


    def create_many(self, newModels: List[RedditModel]):
        try:
            self.collection.insert_many([model.__dict__ for model in newModels])

        except Exception as e:
            raise ValueError(f'Error saving multiple models\nStart: {newModels[0].__dict__}\nEnd:{newModels[-1].__dict__}')


    def get_all(self) -> List[RedditModel]:
        try:
            data = self.collection.find({}, {'_id': 0})
            return [RedditModel(**entry) for entry in data]
        
        except Exception as e:
            raise ValueError(f'Error getting all: {e}')

if __name__ == '__main__':
    import time

    repo = MongoService("localhost", 27017, "testdb", "RedditPosts")

    newPost = RedditModel('test2','test23.com',['test'],68,420, time.time(), "Hello World")
    #print(repo.get_all())
    #print(repo.update(newPost))
    # print(repo.exists(newPost))
    #print(repo.create_update(newPost))
    print(repo.test_connection())