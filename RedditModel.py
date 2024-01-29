from typing import List, Dict
from datetime import datetime, timedelta
import time


class RedditModel:
    def __init__(self,
                 title: str, 
                 url: str,
                 flairs: List[str], 
                 upvotes: int, 
                 num_comments: int, 
                 created: float, 
                 text: str,
                 current_time = None) -> None:
        self.title = title
        self.url = url
        self.flairs = flairs
        self.upvotes = upvotes
        self.num_comments = num_comments
        self.created = created
        self.text = text

        if current_time == None:
            self.current_time = str(timedelta(hours=-8) + datetime.utcfromtimestamp(float(time.time())))



if __name__ == '__main__':

    x = RedditModel('test','test.com',['test'],50,20, time.time(), "Hello World")
    print(x.__dict__)